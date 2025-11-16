from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    """Customer reviews for services"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['service', 'customer']
    
    def __str__(self):
        return f"{self.customer.username} - {self.service.name} ({self.rating}/5)"
