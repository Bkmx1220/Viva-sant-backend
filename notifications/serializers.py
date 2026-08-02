from rest_framework import serializers

from .models import Reminder

# Serializer for the Reminder model
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"
        read_only_fields = ("user",)