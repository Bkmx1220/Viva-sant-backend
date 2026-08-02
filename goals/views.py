from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Goal
from .serializers import GoalSerializer


class GoalView(generics.RetrieveUpdateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        goal, created = Goal.objects.get_or_create(
            user=self.request.user
        )
        return goal