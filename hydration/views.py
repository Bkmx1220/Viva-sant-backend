from datetime import date

from django.db.models import Sum
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils.health import daily_water

from .models import WaterIntake
from .serializers import WaterIntakeSerializer


class WaterIntakeListCreateView(generics.ListCreateAPIView):
    serializer_class = WaterIntakeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WaterIntake.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WaterIntakeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WaterIntakeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WaterIntake.objects.filter(
            user=self.request.user
        )


class TodayWaterView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total = (
            WaterIntake.objects.filter(
                user=request.user,
                date=date.today(),
            ).aggregate(
                total=Sum("quantity")
            )["total"] or 0
        )

        goal = daily_water(request.user.weight)

        return Response(
            {
                "goal_ml": goal,
                "drank_ml": total,
                "remaining_ml": max(goal - total, 0),
                "progress": round((total / goal) * 100, 1) if goal else 0,
            }
        )