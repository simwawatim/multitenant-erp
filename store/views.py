from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'store/login.html')


def home(request):
    return render(request, 'store/login.html')


def login_user(request):
    pass