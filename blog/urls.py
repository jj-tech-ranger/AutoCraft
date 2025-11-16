from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
        path('create/', views.blog_post_create, name='blog_post_create'),
    path('<slug:slug>/update/', views.blog_post_update, name='blog_post_update'),
    path('<slug:slug>/delete/', views.blog_post_delete, name='blog_post_delete'),
]
