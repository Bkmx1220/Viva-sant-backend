from django.conf import settings
from django.db import models


class WaterIntake(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="water_intakes",
    )

    quantity = models.PositiveIntegerField(
        help_text="Quantité en ml"
    )

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.quantity} ml"