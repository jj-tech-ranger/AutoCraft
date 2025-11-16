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

# CRUD Operations
def gallery_image_create(request):
    """Upload a new gallery image"""
    from django.contrib import messages
    from django.shortcuts import redirect
    
    if request.method == 'POST':
        from .forms import GalleryImageForm
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('gallery:gallery_list')
    else:
        from .forms import GalleryImageForm
        form = GalleryImageForm()
    
    return render(request, 'gallery/gallery_form.html', {'form': form})

def gallery_image_update(request, pk):
    """Update gallery image details"""
    from django.contrib import messages
    from django.shortcuts import redirect
    
    image = get_object_or_404(GalleryImage, pk=pk)
    
    if request.method == 'POST':
        from .forms import GalleryImageForm
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image updated successfully!')
            return redirect('gallery:gallery_detail', pk=image.pk)
    else:
        from .forms import GalleryImageForm
        form = GalleryImageForm(instance=image)
    
    return render(request, 'gallery/gallery_form.html', {'form': form, 'image': image})

def gallery_image_delete(request, pk):
    """Delete a gallery image"""
    from django.contrib import messages
    from django.shortcuts import redirect
    
    image = get_object_or_404(GalleryImage, pk=pk)
    
    if request.method == 'POST':
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect('gallery:gallery_list')
    
    return render(request, 'gallery/gallery_confirm_delete.html', {'image': image})
