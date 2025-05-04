from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def login(request):
    return render(request, 'store/login.html')

login_required
def home(request):
    return render(request, 'store/index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password.')
            return redirect('login')
        

login_required
def stores(request):
    return render(request, 'store/stores.html')