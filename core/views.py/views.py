from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import BusinessInfo, ContactMessage
from .forms import ContactForm
from services.models import Service, ServiceCategory
from gallery.models import GalleryImage
from reviews.models import Review
from blog.models import BlogPost

def home(request):
    featured_services = Service.objects.filter(is_active=True, is_featured=True)[:6]
    service_categories = ServiceCategory.objects.filter(is_active=True)[:6]
    featured_images = GalleryImage.objects.filter(is_active=True, is_featured=True)[:8]
    reviews = Review.objects.filter(is_approved=True, is_featured=True)[:6]
    featured_blog_posts = BlogPost.objects.filter(is_published=True, is_featured=True)[:3]
    context = {
        'featured_services': featured_services,
        'service_categories': service_categories,
        'featured_images': featured_images,
        'reviews': reviews,
        'featured_blog_posts': featured_blog_posts,
    }
    return render(request, 'core/home.html', context)

def about(request):
    service_categories = ServiceCategory.objects.filter(is_active=True)
    context = {'service_categories': service_categories}
    return render(request, 'core/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data.get('phone', ''),
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            try:
                send_mail(
                    f"New Contact: {form.cleaned_data['subject']}",
                    f"From: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\n{form.cleaned_data['message']}",
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.NOTIFY_EMAIL],
                    fail_silently=True,
                )
            except:
                pass
            messages.success(request, 'Thank you! We will contact you soon.')
            return redirect('core:contact_success')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'core/contact_success.html')
