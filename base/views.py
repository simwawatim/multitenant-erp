from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='login')
def home(request):
    return render(request, 'base/home.html')


def login(request):
    return render(request, 'base/login.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'base/users.html', context)

@login_required(login_url='login')
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('user-email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = '1234'

        check_email = User.objects.filter(email = email)
        if check_email.exists():
            messages.warning(request, 'Email exists')
            return redirect('users')
        
        check_username = User.objects.filter(username = username)
        if check_username.exists():
            messages.warning(request, 'Username taken')
            return redirect('users')

        User.objects.create_user(username = username, email = email, first_name = first_name, last_name = last_name, password= password)
        messages.success(request, 'User created')
        return redirect('users')
    

def logout_user(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')