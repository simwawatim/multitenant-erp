from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

class Store(TenantMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    def __str__(self):
        return self.domain
    

class Department(models.Model):
    name = models.CharField()
    description = models.CharField()


"""
from store.models import Store, Domain

tenant = Store(
    schema_name='public', 
    name='My First Tenant',
    description='Initial tenant',
    is_active=True
)
tenant.save()

domain = Domain()
domain.domain = 'localhost' 
domain.tenant = tenant
domain.is_primary = True
domain.save()


"""