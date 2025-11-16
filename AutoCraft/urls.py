
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auto.urls')),
        path('services/', include('services.urls')),
        path('bookings/', include('bookings.urls')),
        path('gallery/', include('gallery.urls')),
        path('reviews/', include('reviews.urls')),
        path('blog/', include('blog.urls')),

]
