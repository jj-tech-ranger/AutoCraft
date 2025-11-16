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

# CRUD Views
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ServiceForm

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service created successfully!')
            return redirect('services:service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully!')
            return redirect('services:service_detail', slug=service.slug)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_form.html', {'form': form, 'service': service})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully!')
        return redirect('services:service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})
