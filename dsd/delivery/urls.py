from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer_page, name='customer_page'),
    path('employee', views.employee_page, name='employee_page'),
    path('search_delivery/', views.search_delivery, name='search_delivery'),
    path('create_order/', views.create_order, name='create_order'),
    path('checkout/', views.create_checkout, name='create_checkout'),
]