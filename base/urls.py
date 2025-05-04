from django.urls import path
from django.contrib import admin
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('users/', views.users, name='users'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout-user/', views.logout_user, name='logout_user'),
    path('create-user/', views.create_user, name='create_user'),

]
