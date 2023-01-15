from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Delivery

def is_customer(user):
    return user.groups.filter(name='Customers').exists()

def is_employee(user):
    return user.groups.filter(name='Employees').exists()

def index(request):
    if is_customer(request.user):
        return HttpResponseRedirect("/delivery/customer")
    elif is_employee(request.user):
        return HttpResponseRedirect("/delivery/employee")
    elif request.user.is_superuser:
        return HttpResponseRedirect("/admin")

def customer_page(request):
    button_html = "<button>Click me</button>"
    return render(request, 'delivery.html', {'button': button_html})

def employee_page(request):
    return HttpResponse("Employee page")

def search_delivery(request):
    delivery_id = request.POST.get('delivery_id')
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    return render(request, 'delivery.html', {'delivery': delivery})

