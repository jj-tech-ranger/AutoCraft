from django.urls import path
from auto import views

app_name = 'auto'
urlpatterns = [
    # Authentication
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Jobs
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/create/', views.job_create, name='job_create'),
    path('jobs/<int:pk>/update/', views.job_update, name='job_update'),
    path('jobs/<int:pk>/delete/', views.job_delete, name='job_delete'),
    
    # Customers
    path('customers/', views.job_list, name='customers_list'),

    # Vehicles
    path('vehicles/', views.job_list, name='vehicles_list'),

    # Repairs
    path('repairs/', views.job_list, name='repairs_list'),

    # Bills
    path('bills/', views.job_list, name='bills_list'),

    # Parts
    path('parts/', views.job_list, name='parts_list'),

    # Employees
    path('employees/', views.job_list, name='employees_list'),
]
