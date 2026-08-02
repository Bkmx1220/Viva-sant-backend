from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "activity_type",
        "duration",
        "distance",
        "calories_burned",
        "date",
    )

    list_filter = (
        "activity_type",
        "date",
    )

    search_fields = (
        "user__email",
    )