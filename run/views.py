from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout
from .models import Run

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
import json


def index(request):

    return render(request, "run/index.html")


def login(request):

    return render(request, 'run/login.html')


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_auth(request, user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")



def logout_request(request):
    logout(request)
    response = redirect('/')
    return response


def dashbord(request):
    username = request.user.username
    test = Run.objects.all()
    output = {}
    for i in range(len(test)):
        output[str(i)] = {'distance': str(test[i].distance), 'start_time': str(
            test[i].start_Time), 'end_time': str(test[i].end_time), 'user': str(test[i].user)}
    context = {
        'Runs': output
    }
    return render(request, "run/Dashbord.html", context)


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

    return HttpResponseRedirect("/")

def contact(request):
    return render(request , "run/ContactUs.html")