from datetime import date, timedelta

from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import Activity
from hydration.models import WaterIntake
from nutrition.models import Meal
from nutrition.services import calculate_meal_totals


class StatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        nutrition_stats = []
        activity_stats = []
        hydration_stats = []

        for i in range(6, -1, -1):
            day = date.today() - timedelta(days=i)

            # Nutrition
            meals = Meal.objects.filter(user=user, date=day)

            calories = 0
            for meal in meals:
                totals = calculate_meal_totals(meal)
                calories += totals["calories"]

            nutrition_stats.append({
                "date": day,
                "calories": round(calories, 2),
            })

            # Activité
            activity = Activity.objects.filter(
                user=user,
                date=day,
            ).aggregate(
                total=Sum("calories_burned")
            )["total"] or 0

            activity_stats.append({
                "date": day,
                "calories": activity,
            })

            # Hydratation
            water = WaterIntake.objects.filter(
                user=user,
                date=day,
            ).aggregate(
                total=Sum("quantity")
            )["total"] or 0

            hydration_stats.append({
                "date": day,
                "water": water,
            })

        return Response({
            "last_7_days": {
                "nutrition": nutrition_stats,
                "activity": activity_stats,
                "hydration": hydration_stats,
            }
        })