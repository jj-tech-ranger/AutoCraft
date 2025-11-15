from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q, Sum, F
from django.utils import timezone
from datetime import timedelta
from .models import Customer, Vehicle, Service, Mechanic, RepairJob, Part, JobPart, Payment
from .forms import LoginForm, CustomerForm, VehicleForm, RepairJobForm, PartForm, PaymentForm
from .permissions import is_admin, is_mechanic, is_customer

# Authentication Views
def login_view(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name()}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'auto/login.html', {'form': form})

@login_required
def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# Dashboard Views
@login_required
def dashboard(request):
    """Main dashboard"""
    context = {}
    
    if is_admin(request.user):
        context['total_customers'] = Customer.objects.count()
        context['total_vehicles'] = Vehicle.objects.count()
        context['total_jobs'] = RepairJob.objects.count()
        context['pending_jobs'] = RepairJob.objects.filter(status='PENDING').count()
        context['in_progress_jobs'] = RepairJob.objects.filter(status='IN_PROGRESS').count()
        context['recent_jobs'] = RepairJob.objects.select_related('vehicle', 'mechanic', 'service')[:10]
        context['low_stock_parts'] = Part.objects.filter(quantity__lte=F('reorder_level'))[:5]
        
        last_30_days = timezone.now() - timedelta(days=30)
        context['monthly_revenue'] = Payment.objects.filter(
            status='COMPLETED',
            created_at__gte=last_30_days
        ).aggregate(total=Sum('amount'))['total'] or 0
        
    elif is_mechanic(request.user):
        mechanic = request.user.mechanic_profile
        context['my_jobs'] = RepairJob.objects.filter(
            mechanic=mechanic
        ).select_related('vehicle', 'service').order_by('-scheduled_date')[:10]
        context['pending_jobs'] = context['my_jobs'].filter(status='PENDING').count()
        context['in_progress_jobs'] = context['my_jobs'].filter(status='IN_PROGRESS').count()
        
    elif is_customer(request.user):
        customer = request.user.customer_profile
        context['my_vehicles'] = Vehicle.objects.filter(customer=customer)
        context['my_jobs'] = RepairJob.objects.filter(
            vehicle__customer=customer
        ).select_related('vehicle', 'mechanic', 'service').order_by('-scheduled_date')[:10]
        context['pending_jobs'] = context['my_jobs'].filter(status='PENDING').count()
    
    return render(request, 'auto/dashboard.html', context)

# Job Management Views
@login_required
def job_list(request):
    """List repair jobs"""
    if is_customer(request.user):
        jobs = RepairJob.objects.filter(vehicle__customer=request.user.customer_profile)
    elif is_mechanic(request.user):
        jobs = RepairJob.objects.filter(mechanic=request.user.mechanic_profile)
    else:
        jobs = RepairJob.objects.all()
    
    return render(request, 'auto/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, pk):
    """Job detail view"""
    job = get_object_or_404(RepairJob, pk=pk)
    return render(request, 'auto/job_detail.html', {'job': job})

@login_required
def job_create(request):
    """Create new repair job"""
    if request.method == 'POST':
        form = RepairJobForm(request.POST)
        if form.is_valid():
            job = form.save()
            messages.success(request, 'Repair job created successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = RepairJobForm()
    
    return render(request, 'auto/job_form.html', {'form': form})

@login_required
def job_update(request, pk):
    """Update repair job"""
    job = get_object_or_404(RepairJob, pk=pk)
    
    if request.method == 'POST':
        form = RepairJobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save()
            messages.success(request, 'Repair job updated successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = RepairJobForm(instance=job)
    
    return render(request, 'auto/job_form.html', {'form': form, 'job': job})

@login_required
def job_delete(request, pk):
    """Delete repair job"""
    job = get_object_or_404(RepairJob, pk=pk)
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Repair job deleted successfully!')
        return redirect('job_list')
    
    return render(request, 'auto/job_confirm_delete.html', {'job': job})
