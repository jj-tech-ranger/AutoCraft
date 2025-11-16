from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
    path('create/', views.service_create, name='service_create'),
    path('<slug:slug>/update/', views.service_update, name='service_update'),
    path('<slug:slug>/delete/', views.service_delete, name='service_delete'),
]