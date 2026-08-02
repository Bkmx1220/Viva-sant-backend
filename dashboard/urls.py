from django.urls import path

from .views import DashboardView
# Dashboard URL patterns
urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]