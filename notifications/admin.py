from django.contrib import admin

from .models import Reminder

# Register your models here.
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "reminder_type",
        "reminder_time",
        "is_active",
    )

    list_filter = (
        "reminder_type",
        "is_active",
    )

    search_fields = (
        "user__email",
        "title",
    )