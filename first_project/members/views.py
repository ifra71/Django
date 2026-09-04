from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

def members(request):
    template = loader.get_template('my_first.html')
    return HttpResponse(template.render())

def members(request):
    if request.method == "GET":
        return HttpResponse("Here are the members")

def members(request):
    if request.method == "POST":
        name = request.POST["name"]
        return HttpResponse("Received " + name)