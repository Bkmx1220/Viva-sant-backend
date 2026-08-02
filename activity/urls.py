from django.urls import path

from .views import (
    ActivityDetailView,
    ActivityListCreateView,
    TodayActivityView,
)

urlpatterns = [
    path(
        "",
        ActivityListCreateView.as_view(),
    ),
    path(
        "today/",
        TodayActivityView.as_view(),
    ),
    path(
        "<int:pk>/",
        ActivityDetailView.as_view(),
    ),
]