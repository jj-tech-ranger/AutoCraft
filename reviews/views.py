from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from services.models import Service

def review_list(request):
    """Display all approved reviews"""
    reviews = Review.objects.filter(is_approved=True)
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

@login_required
def review_create(request, service_id):
    """Create a review for a service"""
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        
        Review.objects.create(
            service=service,
            customer=request.user,
            rating=rating,
            title=title,
            comment=comment
        )
        
        messages.success(request, 'Thank you for your review! It will be published after approval.')
        return redirect('services:service_detail', pk=service_id)
    
    return render(request, 'reviews/review_form.html', {'service': service})
