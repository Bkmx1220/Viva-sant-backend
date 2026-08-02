from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    bmi = serializers.FloatField(allow_null=True)
    bmi_category = serializers.CharField(allow_null=True)
    weight = serializers.FloatField(allow_null=True)
    height = serializers.FloatField(allow_null=True)
    health_goal = serializers.CharField()
    daily_water_ml = serializers.IntegerField()
    recommended_calories = serializers.IntegerField()