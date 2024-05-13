from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


# Register your models here.
admin.site.site_header='Empresa X Dashboard'
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','cantidad')
    list_filter=['category']




admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)
