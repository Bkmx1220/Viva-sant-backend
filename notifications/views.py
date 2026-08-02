from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Reminder
from .serializers import ReminderSerializer

# Reminder List and Create Views
class ReminderListCreateView(generics.ListCreateAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

# Reminder Detail, Update, and Delete Views
class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(
            user=self.request.user
        )