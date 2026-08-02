from django.conf import settings
from django.db import models


class Activity(models.Model):
    WALKING = "walking"
    RUNNING = "running"
    CYCLING = "cycling"
    SWIMMING = "swimming"
    YOGA = "yoga"
    GYM = "gym"

    ACTIVITY_CHOICES = [
        (WALKING, "Marche"),
        (RUNNING, "Course"),
        (CYCLING, "Vélo"),
        (SWIMMING, "Natation"),
        (YOGA, "Yoga"),
        (GYM, "Musculation"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activities",
    )

    activity_type = models.CharField(
        max_length=20,
        choices=ACTIVITY_CHOICES,
    )

    duration = models.PositiveIntegerField(
        help_text="Durée en minutes"
    )

    distance = models.FloatField(
        blank=True,
        null=True,
        help_text="Distance en kilomètres",
    )

    calories_burned = models.FloatField(default=0)

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.activity_type}"