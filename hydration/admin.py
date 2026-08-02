from django.contrib import admin

from .models import WaterIntake


@admin.register(WaterIntake)
class WaterIntakeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "quantity",
        "date",
    )

    list_filter = (
        "date",
    )

    search_fields = (
        "user__email",
    )