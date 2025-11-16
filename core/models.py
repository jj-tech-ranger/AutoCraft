from django.db import models
from django.core.validators import EmailValidator

class BusinessInfo(models.Model):
    """Single instance model for business information"""
    businessname = models.CharField(max_length=200, default='AUTOCRAFT CENTER')
    tagline = models.CharField(max_length=300)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Kenya')
    
    # Business Hours
    monday_hours = models.CharField(max_length=50, default='8:00 AM - 6:00 PM')
    tuesday_hours = models.CharField(max_length=50, default='8:00 AM - 6:00 PM')
    wednesday_hours = models.CharField(max_length=50, default='8:00 AM - 6:00 PM')
    thursday_hours = models.CharField(max_length=50, default='8:00 AM - 6:00 PM')
    friday_hours = models.CharField(max_length=50, default='8:00 AM - 6:00 PM')
    saturday_hours = models.CharField(max_length=50, default='9:00 AM - 4:00 PM')
    sunday_hours = models.CharField(max_length=50, default='Closed')
    
    # Social Media
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    # SEO
    meta_description = models.TextField(max_length=160)
    meta_keywords = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'businessinfo'
        verbose_name = 'Business Information'
        verbose_name_plural = 'Business Information'
    
    def __str__(self):
        return self.businessname

class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'contactmessages'
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
