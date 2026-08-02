from django.conf import settings
from django.db import models

# Modèle pour représenter un aliment
class Food(models.Model):
    name = models.CharField(max_length=150, unique=True)

    calories = models.FloatField(help_text="Calories pour 100 g")
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fat = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Meal(models.Model):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

    MEAL_CHOICES = [
        (BREAKFAST, "Petit-déjeuner"),
        (LUNCH, "Déjeuner"),
        (DINNER, "Dîner"),
        (SNACK, "Collation"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="meals",
    )

    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_CHOICES,
    )

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.meal_type}"

#
class MealItem(models.Model):
    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name="items",
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
    )

    quantity = models.FloatField(
        help_text="Quantité en grammes"
    )

    def __str__(self):
        return f"{self.food.name} ({self.quantity} g)"