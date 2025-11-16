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

# CRUD Operations  
def review_update(request, pk):
    """Update an existing review"""
    from django.contrib import messages
    from django.shortcuts import redirect
    
    review = get_object_or_404(Review, pk=pk, customer=request.user)
    
    if request.method == 'POST':
        from .forms import ReviewForm
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('reviews:review_list')
    else:
        from .forms import ReviewForm
        form = ReviewForm(instance=review)
    
    return render(request, 'reviews/review_form.html', {'form': form, 'review': review})

def review_delete(request, pk):
    """Delete a review"""
    from django.contrib import messages
    from django.shortcuts import redirect
    
    review = get_object_or_404(Review, pk=pk, customer=request.user)
    
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('reviews:review_list')
    
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})
