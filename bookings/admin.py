from django.contrib import admin
from .models import Booking, TimeSlot

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['time', 'is_available']
    list_filter = ['is_available']
    list_editable = ['is_available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'service', 'booking_date', 'time_slot', 'status', 'created_at']
    list_filter = ['status', 'booking_date', 'created_at']
    search_fields = ['customer__username', 'customer__email', 'service__name']
    date_hierarchy = 'booking_date'
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('customer', 'service', 'booking_date', 'time_slot')
        }),
        ('Status & Notes', {
            'fields': ('status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
