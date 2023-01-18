from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer_page, name='customer_page'),
    path('employee/', views.employee_page, name='employee_page'),
    path('search_delivery/', views.search_delivery, name='search_delivery'),
    path('create_order/', views.create_order, name='create_order'),
    path('checkout/', views.create_checkout, name='create_checkout'),
    path('update_delivery/',views.update_delivery,name='update_delivery'),
    path('get_overview_deliveries/',views.get_overview_deliveries,name='get_overview_deliveries')
]