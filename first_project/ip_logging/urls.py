from django.urls import path
from .views import (
    HomeView,
    ProfileView,
    DashboardView,
)


urlpatterns = [
    path("home/", HomeView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("dashboard/", DashboardView.as_view()),
]