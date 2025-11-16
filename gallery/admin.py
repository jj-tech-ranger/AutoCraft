from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'order', 'created_at']
    list_filter = ['is_featured', 'category', 'created_at']
    search_fields = ['title', 'description', 'category']
    list_editable = ['is_featured', 'order']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image', 'description')
        }),
        ('Categorization & Display', {
            'fields': ('category', 'is_featured', 'order')
        }),
    )
