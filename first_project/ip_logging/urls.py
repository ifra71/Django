from django.urls import path

from .views import DashboardView, HomeView, ProfileView, UserLoginView, UserLogoutView

urlpatterns = [
    path("", HomeView.as_view()),
    path("home/", HomeView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("dashboard/", DashboardView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("logout/", UserLogoutView.as_view()),
]
