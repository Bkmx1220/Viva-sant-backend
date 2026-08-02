from django.conf import settings
from django.db import models

# Modèle pour représenter un rappel
class Reminder(models.Model):
    WATER = "water"
    MEAL = "meal"
    ACTIVITY = "activity"
    SLEEP = "sleep"

    REMINDER_CHOICES = [
        (WATER, "Hydratation"),
        (MEAL, "Repas"),
        (ACTIVITY, "Activité"),
        (SLEEP, "Sommeil"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reminders",
    )

    reminder_type = models.CharField(
        max_length=20,
        choices=REMINDER_CHOICES,
    )

    title = models.CharField(max_length=100)

    message = models.TextField()

    reminder_time = models.TimeField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.title}"