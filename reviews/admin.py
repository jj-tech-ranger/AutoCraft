from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['service', 'customer', 'rating', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'rating', 'created_at']
    search_fields = ['customer__username', 'service__name', 'title', 'comment']
    list_editable = ['is_approved']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Review Information', {
            'fields': ('service', 'customer', 'rating')
        }),
        ('Content', {
            'fields': ('title', 'comment')
        }),
        ('Status', {
            'fields': ('is_approved', 'created_at')
        }),
    )
