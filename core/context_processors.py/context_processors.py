from .models import BusinessInfo

def business_info(request):
    try:
        info = BusinessInfo.objects.filter(is_active=True).first()
        return {'business_info': info}
    except:
        return {'business_info': None}
