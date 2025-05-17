from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from store.models import Store, Domain


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
    stores = Store.objects.filter()
    context = {
        'stores': stores
    }
    return render(request, 'store/stores.html', context)

def employees(request):

    return render(request, 'store/employee.html')


def create_store(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
    
        tenant = Store.objects.create(
                        schema_name= name,
                        name= name,
                        description = description,
                        is_active=True)
        tenant.save() 
        domain = Domain()
        domain.domain = f'{name}.localhost' 
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()

    messages.success(request, 'Store created successfully')
    return redirect('stores')



def update_store(request, id):
    store = get_object_or_404(Store, id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        store.name = name
        store.description = description
        store.save()
        messages.success(request, "Store updated successfully")

        return redirect('stores') 
    
def update_store_status(request, id, status):
    store = get_object_or_404(Store, id=id)
    store.is_active = status.lower() == 'true' 
    store.save()
    messages.success(request, "Store status updated successfully")
    return redirect('stores')  



