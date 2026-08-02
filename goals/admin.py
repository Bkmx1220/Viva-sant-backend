from django.contrib import admin

from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "target_weight",
        "daily_calories",
        "daily_water",
        "daily_activity_minutes",
        "daily_steps",
    )