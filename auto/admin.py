from django.contrib import admin
from auto.models import Customer, Vehicle, Service, Mechanic, RepairJob, Part, JobPart, Payment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'created_at']
    list_filter = ['city', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'phone']
    date_hierarchy = 'created_at'

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'make', 'model', 'year', 'customer', 'created_at']
    list_filter = ['make', 'year', 'created_at']
    search_fields = ['license_plate', 'vin', 'make', 'model']
    date_hierarchy = 'created_at'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'duration_hours', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']

@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization', 'hourly_rate', 'is_available']
    list_filter = ['specialization', 'is_available']
    search_fields = ['user__first_name', 'user__last_name']

@admin.register(RepairJob)
class RepairJobAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicle', 'mechanic', 'service', 'status', 'priority', 'scheduled_date']
    list_filter = ['status', 'priority', 'scheduled_date']
    search_fields = ['vehicle__license_plate', 'description']
    date_hierarchy = 'scheduled_date'

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'part_number', 'quantity', 'unit_price', 'supplier']
    list_filter = ['supplier']
    search_fields = ['name', 'part_number']

@admin.register(JobPart)
class JobPartAdmin(admin.ModelAdmin):
    list_display = ['job', 'part', 'quantity', 'unit_price']
    list_filter = ['created_at']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'job', 'amount', 'payment_method', 'status', 'created_at']
    list_filter = ['payment_method', 'status', 'created_at']
    search_fields = ['transaction_id']
    date_hierarchy = 'created_at'
