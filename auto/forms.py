from django import forms
from auto.models import Customer, Vehicle, RepairJob, Part, Payment

class LoginForm(forms.Form):
    """User login form"""
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class CustomerForm(forms.ModelForm):
    """Customer creation/edit form"""
    class Meta:
        model = Customer
        fields = ['phone', 'address', 'city']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VehicleForm(forms.ModelForm):
    """Vehicle creation/edit form"""
    class Meta:
        model = Vehicle
        fields = ['customer', 'make', 'model', 'year', 'license_plate', 'vin', 'color', 'mileage']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'vin': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RepairJobForm(forms.ModelForm):
    """Repair job creation/edit form"""
    class Meta:
        model = RepairJob
        fields = ['vehicle', 'mechanic', 'service', 'status', 'priority', 'description', 'estimated_cost', 'actual_cost', 'scheduled_date', 'notes']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'mechanic': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estimated_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'actual_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'scheduled_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PartForm(forms.ModelForm):
    """Part creation/edit form"""
    class Meta:
        model = Part
        fields = ['name', 'part_number', 'description', 'quantity', 'unit_price', 'supplier', 'reorder_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'part_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control'}),
            'reorder_level': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PaymentForm(forms.ModelForm):
    """Payment form"""
    class Meta:
        model = Payment
        fields = ['job', 'amount', 'payment_method', 'status', 'transaction_id', 'notes']
        widgets = {
            'job': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
