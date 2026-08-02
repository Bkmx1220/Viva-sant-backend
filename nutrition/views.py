from datetime import date

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Food, Meal, MealItem
from .services import calculate_meal_totals
from .serializers import (
    FoodSerializer,
    MealSerializer,
    MealItemSerializer,
)
from rest_framework.views import APIView

# Food Views
class FoodListCreateView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]


class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]


class MealListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)


class MealItemCreateView(generics.CreateAPIView):
    queryset = MealItem.objects.all()
    serializer_class = MealItemSerializer
    permission_classes = [IsAuthenticated]


class MealItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealItem.objects.all()
    serializer_class = MealItemSerializer
    permission_classes = [IsAuthenticated]

# View for retrieving today's nutrition summary
class TodayNutritionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        meals = Meal.objects.filter(
            user=request.user,
            date=date.today()
        )

        summary = {
            "calories": 0,
            "protein": 0,
            "carbs": 0,
            "fat": 0,
        }

        for meal in meals:
            totals = calculate_meal_totals(meal)

            summary["calories"] += totals["calories"]
            summary["protein"] += totals["protein"]
            summary["carbs"] += totals["carbs"]
            summary["fat"] += totals["fat"]

        return Response({
            "date": date.today(),
            "total_calories": round(summary["calories"], 2),
            "total_protein": round(summary["protein"], 2),
            "total_carbs": round(summary["carbs"], 2),
            "total_fat": round(summary["fat"], 2),
        })
    