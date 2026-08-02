from datetime import date

from django.db.models import Sum
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Activity
from .serializers import ActivitySerializer
from .services import calculate_calories


class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        activity = serializer.save(
            user=self.request.user
        )

        activity.calories_burned = calculate_calories(
            activity.activity_type,
            activity.duration,
        )

        activity.save()


class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        activity = serializer.save()

        activity.calories_burned = calculate_calories(
            activity.activity_type,
            activity.duration,
        )

        activity.save()

# View for retrieving today's activities and their aggregated statistics
class TodayActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        activities = Activity.objects.filter(
            user=request.user,
            date=date.today(),
        )

        total_duration = (
            activities.aggregate(
                total=Sum("duration")
            )["total"] or 0
        )

        total_distance = (
            activities.aggregate(
                total=Sum("distance")
            )["total"] or 0
        )

        total_calories = (
            activities.aggregate(
                total=Sum("calories_burned")
            )["total"] or 0
        )

        return Response(
            {
                "date": date.today(),
                "total_activities": activities.count(),
                "total_duration": total_duration,
                "total_distance": total_distance,
                "total_calories": total_calories,
            }
        )