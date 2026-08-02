from rest_framework import serializers

from .models import Food, Meal, MealItem

from .services import calculate_meal_totals

# Serializers for the nutrition app
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"

# Serializer for the MealItem model with a read-only field for the food name
class MealItemSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source="food.name", read_only=True)

    class Meta:
        model = MealItem
        fields = (
            "id",
            "meal",
            "food",
            "food_name",
            "quantity",
        )

# Serializer for the Meal model with nested MealItemSerializer and calculated nutritional totals
class MealSerializer(serializers.ModelSerializer):
    items = MealItemSerializer(many=True, read_only=True)

    total_calories = serializers.SerializerMethodField()
    total_protein = serializers.SerializerMethodField()
    total_carbs = serializers.SerializerMethodField()
    total_fat = serializers.SerializerMethodField()
# Serializer for the Meal model with nested MealItemSerializer and calculated nutritional totals
    class Meta:
        model = Meal
        fields = (
            "id",
            "meal_type",
            "date",
            "items",
            "total_calories",
            "total_protein",
            "total_carbs",
            "total_fat",
        )

    def _totals(self, obj):
        return calculate_meal_totals(obj)

    def get_total_calories(self, obj):
        return self._totals(obj)["calories"]

    def get_total_protein(self, obj):
        return self._totals(obj)["protein"]

    def get_total_carbs(self, obj):
        return self._totals(obj)["carbs"]

    def get_total_fat(self, obj):
        return self._totals(obj)["fat"]