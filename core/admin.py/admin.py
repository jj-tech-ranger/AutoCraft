from django.contrib import admin
from .models import BusinessInfo, ContactMessage

@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'email', 'phone']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
