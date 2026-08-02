from django.urls import path

from .views import (
    FoodDetailView,
    FoodListCreateView,
    MealDetailView,
    MealItemCreateView,
    MealItemDetailView,
    MealListCreateView,
    TodayNutritionView,
)

urlpatterns = [
    path("foods/", FoodListCreateView.as_view()),
    path("foods/<int:pk>/", FoodDetailView.as_view()),

    path("meals/", MealListCreateView.as_view()),
    path("meals/<int:pk>/", MealDetailView.as_view()),

    path("meal-items/", MealItemCreateView.as_view()),
    path("meal-items/<int:pk>/", MealItemDetailView.as_view()),
    path("today/", TodayNutritionView.as_view()),
]