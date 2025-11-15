from django.contrib.auth.models import Group

def is_admin(user):
    """Check if user is admin"""
    return user.is_staff or user.is_superuser or user.groups.filter(name='Admin').exists()

def is_mechanic(user):
    """Check if user is mechanic"""
    return hasattr(user, 'mechanic_profile') or user.groups.filter(name='Mechanic').exists()

def is_customer(user):
    """Check if user is customer"""
    return hasattr(user, 'customer_profile') or user.groups.filter(name='Customer').exists()

def has_job_access(user, job):
    """Check if user has access to a specific job"""
    if is_admin(user):
        return True
    elif is_mechanic(user) and job.mechanic == user.mechanic_profile:
        return True
    elif is_customer(user) and job.vehicle.customer == user.customer_profile:
        return True
    return False
