from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

# from django.shortcuts import HttpResponse2

# Create your views here.

def index(request):
# return HttpResponse("<h1>My first Webpage with python Django</h1>")
   return HttpResponse("<h1>Using shortcuts.My first Webpage with python Django</h1>")