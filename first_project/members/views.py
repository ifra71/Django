from django.shortcuts import render
from django.views import View


class HomeView(View):

    def get(self, request):
        context = {"name": "ifra", "age": 22}

        return render(request, "members/home.html", context)


class AboutView(View):

    def get(self, request):

        return render(request, "members/about.html")
