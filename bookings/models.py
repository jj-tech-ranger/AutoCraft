from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class TimeSlot(models.Model):
    """Available time slots for bookings"""
    time = models.TimeField()
    is_available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['time']
    
    def __str__(self):
        return self.time.strftime('%I:%M %p')

class Booking(models.Model):
    """Customer service bookings"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-booking_date', '-created_at']
        unique_together = ['booking_date', 'time_slot']
    
    def __str__(self):
        return f"{self.customer.username} - {self.service.name} - {self.booking_date}"
