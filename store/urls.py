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
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)