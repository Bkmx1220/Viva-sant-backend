from datetime import date

from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import Activity
from common.utils.health import (
    bmi_category,
    calculate_bmi,
    daily_water,
)
from goals.models import Goal
from hydration.models import WaterIntake
from nutrition.models import Meal
from nutrition.services import calculate_meal_totals


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # -------- Nutrition --------
        meals = Meal.objects.filter(
            user=user,
            date=date.today(),
        )

        nutrition = {
            "calories": 0,
            "protein": 0,
            "carbs": 0,
            "fat": 0,
        }

        for meal in meals:
            totals = calculate_meal_totals(meal)

            nutrition["calories"] += totals["calories"]
            nutrition["protein"] += totals["protein"]
            nutrition["carbs"] += totals["carbs"]
            nutrition["fat"] += totals["fat"]

        nutrition = {
            "calories": round(nutrition["calories"], 2),
            "protein": round(nutrition["protein"], 2),
            "carbs": round(nutrition["carbs"], 2),
            "fat": round(nutrition["fat"], 2),
        }

        # -------- Activités --------
        activities = Activity.objects.filter(
            user=user,
            date=date.today(),
        )

        activity = {
            "count": activities.count(),
            "duration": activities.aggregate(
                total=Sum("duration")
            )["total"] or 0,
            "distance": activities.aggregate(
                total=Sum("distance")
            )["total"] or 0,
            "calories": activities.aggregate(
                total=Sum("calories_burned")
            )["total"] or 0,
        }

        # -------- Hydratation --------
        water_drank = (
            WaterIntake.objects.filter(
                user=user,
                date=date.today(),
            ).aggregate(
                total=Sum("quantity")
            )["total"] or 0
        )

        water_goal = daily_water(user.weight)

        hydration = {
            "goal_ml": water_goal,
            "drank_ml": water_drank,
            "remaining_ml": max(water_goal - water_drank, 0),
            "progress": round((water_drank / water_goal) * 100, 1)
            if water_goal else 0,
        }

        goal, _ = Goal.objects.get_or_create(user=user)

        goals = {
            "calories": {
                "target": goal.daily_calories,
                "current": nutrition["calories"],
                "remaining": max(
                    goal.daily_calories - nutrition["calories"],
                    0,
                ),
                "progress": round(
                    (nutrition["calories"] / goal.daily_calories) * 100,
                    1,
                ) if goal.daily_calories else 0,
            },
            "water": {
                "target": goal.daily_water,
                "current": hydration["drank_ml"],
                "remaining": max(
                    goal.daily_water - hydration["drank_ml"],
                    0,
                ),
                "progress": round(
                    (hydration["drank_ml"] / goal.daily_water) * 100,
                    1,
                ) if goal.daily_water else 0,
            },
            "activity": {
                "target": goal.daily_activity_minutes,
                "current": activity["duration"],
                "remaining": max(
                    goal.daily_activity_minutes - activity["duration"],
                    0,
                ),
                "progress": round(
                    (activity["duration"] / goal.daily_activity_minutes) * 100,
                    1,
                ) if goal.daily_activity_minutes else 0,
            },
        }

        bmi = calculate_bmi(user.height, user.weight)

        return Response(
            {
                "user": {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "height": user.height,
                    "weight": user.weight,
                    "health_goal": user.health_goal,
                    "bmi": bmi,
                    "bmi_category": bmi_category(bmi),
                    "daily_water_ml": water_goal,
                },

                "nutrition": nutrition,

                "activity": activity,

                "hydration": hydration,

                "goals": goals,

                "calorie_balance": round(
                    nutrition["calories"] - activity["calories"],
                    2,
                ),
            }
        )