from django.urls import path

from .views import (
    ReminderDetailView,
    ReminderListCreateView,
)

urlpatterns = [
    path(
        "",
        ReminderListCreateView.as_view(),
    ),
    path(
        "<int:pk>/",
        ReminderDetailView.as_view(),
    ),
]