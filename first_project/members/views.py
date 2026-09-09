from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {
        "name" : "ifra",
        "age" : 22
    }
    return render(request, "members/home.html", context)

def about(request):
    return render(request, "members/about.html")