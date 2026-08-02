from django.conf import settings
from django.db import models


class Goal(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="goal",
    )

    target_weight = models.FloatField(
        blank=True,
        null=True,
        help_text="Poids cible en kg",
    )

    daily_calories = models.PositiveIntegerField(
        default=2200,
    )

    daily_water = models.PositiveIntegerField(
        default=2500,
        help_text="Objectif d'eau en ml",
    )

    daily_activity_minutes = models.PositiveIntegerField(
        default=30,
    )

    daily_steps = models.PositiveIntegerField(
        default=10000,
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Objectifs de {self.user.email}"