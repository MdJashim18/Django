from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    return render(request,"navigation/about.html")
def home(request):
    return render(request,"navigation/home.html")