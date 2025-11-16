from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import GalleryImage

def gallery_list(request):
    """Display gallery images"""
    category = request.GET.get('category')
    
    if category:
        images = GalleryImage.objects.filter(category=category)
    else:
        images = GalleryImage.objects.all()
    
    paginator = Paginator(images, 12)  # 12 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = GalleryImage.objects.values_list('category', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'gallery/gallery_list.html', context)

def gallery_detail(request, pk):
    """Display single gallery image details"""
    image = get_object_or_404(GalleryImage, pk=pk)
    return render(request, 'gallery/gallery_detail.html', {'image': image})
