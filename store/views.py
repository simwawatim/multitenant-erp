from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from store.helpers.create_password import generate_user_password
from store.helpers.random_username import generate_user_username
from store.models import Store, Domain, Department
from django.contrib.auth.models import User
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
    stores = Store.objects.all()
    store_data = []
    for store in stores:
        domain = Domain.objects.filter(tenant=store).first()
        store_data.append({
            'store': store,
            'domain': domain
        })
    return render(request, 'store/stores.html', {'stores': store_data})


def employees(request):
    employees = User.objects.all()

    context = {
        'employees': employees
    }
    return render(request, 'store/employee.html', context)


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


def create_main_store_employees(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = generate_user_username(request)
        password = generate_user_password(request)

        check_email_if_exists = User.objects.filter(email = email)
        if check_email_if_exists.exists():
            messages.warning(request, 'User email already exists')
            return redirect('employees')
        
        else:
            create_user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password
            )
            messages.success(request, 'User created succussfully')
            return redirect('employees')


def admin_update_employee(request, id):
    employee = get_object_or_404(User, id=id)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_email = request.POST.get('email')

        employee.first_name = first_name
        employee.last_name = last_name
        employee.email = user_email

        employee.save()

        messages.success(request, 'Employee profile updated successfully')
        return redirect('employees')
    else:
        messages.warning(request, 'Error update successfully')
        return redirect('employees')
    
def update_user_status(request, id, status):
    employee = get_object_or_404(User, id=id)
    employee.is_active = status.lower() == 'true' 
    employee.save()
    messages.success(request, 'User status updated succussfully')
    return redirect('employees')


    
def departements(request):
    departments = Department.objects.all()
    contex = {
        'departments': departments
    }
    return render(request, 'store/departments.html', contex)