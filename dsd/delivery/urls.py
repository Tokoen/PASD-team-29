from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer_page, name='customer_page'),
    path('employee', views.employee_page, name='employee_page'),
    path('search_delivery/', views.search_delivery, name='search_delivery'),
]