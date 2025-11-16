from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_from', 'is_featured', 'is_active', 'order']
    list_filter = ['category', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured', 'is_active', 'order']
