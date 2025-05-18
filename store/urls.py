from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('stores/', views.stores, name='stores'),
    path('employees/', views.employees, name='employees'),
    path('login_user', views.login_user, name='login_user'),
    path('create_store/', views.create_store, name='create_store'),
    path('stores/update-store/<int:id>/', views.update_store, name='update_store'),
    path('admin-update-employee/<int:id>/', views.admin_update_employee, name='admin_update_employee'),
    path('update-user-status/<int:id>/<str:status>/', views.update_user_status, name='update_user_status'),
    path('create-main-store-employees/', views.create_main_store_employees, name='create_main_store_employees'),
    path('store/update-store-status/<int:id>/<str:status>/', views.update_store_status, name='update_store_status'),
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)