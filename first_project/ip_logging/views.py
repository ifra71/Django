from django.http import HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request):
        return HttpResponse("Home endpoint")


class ProfileView(View):
    def get(self, request):
        return HttpResponse("Profile endpoint")


class DashboardView(View):
    def get(self, request):
        return HttpResponse("Dashboard endpoint")

