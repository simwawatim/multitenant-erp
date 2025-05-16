from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def login(request):
    return render(request, 'store/login.html')

def home(request):
    return render(request, 'store/index.html')


def login_user(request):
    print('post received')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password, 'triggered 1')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print(1)
            return redirect('home')
        else:
            print(0)
            messages.warning(request, 'Invalid username or password.')
            return redirect('login')
    
def stores(request):
    return render(request, 'store/stores.html')