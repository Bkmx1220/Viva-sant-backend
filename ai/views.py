from datetime import date

from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import Activity
from goals.models import Goal
from hydration.models import WaterIntake
from nutrition.models import Meal
from nutrition.services import calculate_meal_totals

# Vue pour fournir des recommandations personnalisées
class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        goal, _ = Goal.objects.get_or_create(user=user)

        recommendations = []

        # ---------- Nutrition ----------
        meals = Meal.objects.filter(
            user=user,
            date=date.today(),
        )

        calories = 0
        protein = 0

        for meal in meals:
            totals = calculate_meal_totals(meal)
            calories += totals["calories"]
            protein += totals["protein"]

        if calories < goal.daily_calories * 0.8:
            recommendations.append({
                "type": "nutrition",
                "title": "Calories",
                "message": "Vous êtes en dessous de votre objectif calorique aujourd'hui."
            })

        if protein < 60:
            recommendations.append({
                "type": "nutrition",
                "title": "Protéines",
                "message": "Essayez d'ajouter davantage d'aliments riches en protéines."
            })

        # ---------- Hydratation ----------
        water = (
            WaterIntake.objects.filter(
                user=user,
                date=date.today(),
            ).aggregate(
                total=Sum("quantity")
            )["total"] or 0
        )

        if water < goal.daily_water:
            recommendations.append({
                "type": "hydration",
                "title": "Hydratation",
                "message": f"Il vous reste {goal.daily_water - water} ml d'eau à boire aujourd'hui."
            })

        # ---------- Activité ----------
        duration = (
            Activity.objects.filter(
                user=user,
                date=date.today(),
            ).aggregate(
                total=Sum("duration")
            )["total"] or 0
        )

        if duration < goal.daily_activity_minutes:
            recommendations.append({
                "type": "activity",
                "title": "Activité",
                "message": f"Encore {goal.daily_activity_minutes - duration} minutes d'activité pour atteindre votre objectif."
            })

        if not recommendations:
            recommendations.append({
                "type": "success",
                "title": "Bravo",
                "message": "Vous avez atteint tous vos objectifs aujourd'hui !"
            })

        return Response({
            "recommendations": recommendations
        })