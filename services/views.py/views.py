from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory

def service_list(request):
    services = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects.filter(is_active=True)
    context = {
        'services': services,
        'categories': categories,
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related_services = Service.objects.filter(
        category=service.category,
        is_active=True
    ).exclude(id=service.id)[:3]
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)

def category_services(request, slug):
    category = get_object_or_404(ServiceCategory, slug=slug, is_active=True)
    services = Service.objects.filter(category=category, is_active=True)
    context = {
        'category': category,
        'services': services,
    }
    return render(request, 'services/category_services.html', context)
