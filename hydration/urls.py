from django.urls import path

from .views import (
    TodayWaterView,
    WaterIntakeDetailView,
    WaterIntakeListCreateView,
)

urlpatterns = [
    path(
        "",
        WaterIntakeListCreateView.as_view(),
    ),
    path(
        "today/",
        TodayWaterView.as_view(),
    ),
    path(
        "<int:pk>/",
        WaterIntakeDetailView.as_view(),
    ),
]