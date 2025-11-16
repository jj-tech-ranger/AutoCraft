from django.db import models

class GalleryImage(models.Model):
    """Gallery images showcasing completed work"""
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']
        verbose_name_plural = 'Gallery Images'
    
    def __str__(self):
        return self.title
