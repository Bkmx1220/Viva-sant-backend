from .models import Meal

# Fonction pour calculer les valeurs nutritionnelles totales d'un repas
def calculate_meal_totals(meal: Meal):
    """
    Calcule les valeurs nutritionnelles totales d'un repas.
    """
    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
    }

    for item in meal.items.select_related("food"):
        factor = item.quantity / 100

        totals["calories"] += item.food.calories * factor
        totals["protein"] += item.food.protein * factor
        totals["carbs"] += item.food.carbs * factor
        totals["fat"] += item.food.fat * factor

    return {
        "calories": round(totals["calories"], 2),
        "protein": round(totals["protein"], 2),
        "carbs": round(totals["carbs"], 2),
        "fat": round(totals["fat"], 2),
    }