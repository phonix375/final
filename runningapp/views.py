from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
   return render(request,'runningapp/index.html')


def login(request) : 
   return render(request,'runningapp/login.html')