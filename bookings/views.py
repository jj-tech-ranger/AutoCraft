from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Booking, TimeSlot
from services.models import Service

@login_required
def booking_list(request):
    """Display list of user's bookings"""
    bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_create(request, service_id):
    """Create a new booking"""
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        time_slot_id = request.POST.get('time_slot')
        notes = request.POST.get('notes', '')
        
        time_slot = get_object_or_404(TimeSlot, id=time_slot_id)
        
        booking = Booking.objects.create(
            customer=request.user,
            service=service,
            booking_date=booking_date,
            time_slot=time_slot,
            notes=notes
        )
        
        messages.success(request, 'Booking created successfully!')
        return redirect('bookings:booking_detail', pk=booking.pk)
    
    time_slots = TimeSlot.objects.filter(is_available=True)
    context = {
        'service': service,
        'time_slots': time_slots,
    }
    return render(request, 'bookings/booking_create.html', context)

@login_required
def booking_detail(request, pk):
    """Display booking details"""
    booking = get_object_or_404(Booking, pk=pk, customer=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

@login_required
def booking_cancel(request, pk):
    """Cancel a booking"""
    booking = get_object_or_404(Booking, pk=pk, customer=request.user)
    
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
        return redirect('bookings:booking_list')
    
    return render(request, 'bookings/booking_cancel.html', {'booking': booking})
