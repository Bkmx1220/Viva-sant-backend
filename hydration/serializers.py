from rest_framework import serializers

from .models import WaterIntake


class WaterIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterIntake
        fields = "__all__"
        read_only_fields = ("user",)