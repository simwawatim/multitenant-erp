from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Store, Domain

@admin.register(Store)
class StoreAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    search_fields = ('domain',)
    list_filter = ('is_primary',)
