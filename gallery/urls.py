from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('<int:pk>/', views.gallery_detail, name='gallery_detail'),
        path('create/', views.gallery_image_create, name='gallery_image_create'),
    path('<int:pk>/update/', views.gallery_image_update, name='gallery_image_update'),
    path('<int:pk>/delete/', views.gallery_image_delete, name='gallery_image_delete'),
]
