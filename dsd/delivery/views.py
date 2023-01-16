from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *


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
    return render(request, 'customer.html')

def employee_page(request):
    return HttpResponse("Employee page")

def search_delivery(request):
    if request.POST.get('delivery_id'):
        delivery_id = request.POST.get('delivery_id')
        delivery = get_object_or_404(Delivery, pk=delivery_id)
        return render(request, 'search_delivery.html', {'delivery': delivery})
    return render(request, 'search_delivery.html')

def create_order(request):
    if request.POST.get('delivery_id'):
        send_date = request.POST.get['send_date']
        x_in_mm = request.POST.get['x_in_mm']
        y_in_mm = request.POST.get['y_in_mm']
        z_in_mm = request.POST.get['z_in_mm']
        is_breakable = request.POST.get['s_breakable']
        is_perishable = request.POST.get['is_perishable']
        sender_name = request.POST.get['sender_name']
        sender_address = request.POST.get['sender_address']
        sender_zipcode = request.POST.get['sender_zipcode']
        sender_city = request.POST.get['sender_city ']
        sender_country = request.POST.get['sender_country']
        receiver_name = request.POST.get['receiver_name']
        receiver_address = request.POST.get['receiver_address']
        receiver_zipcode = request.POST.get['receiver_zipcode']
        receiver_city = request.POST.get['receiver_city']
        receiver_country = request.POST.get['receiver_country']
        sender_info = Sender_Info(sender_name, sender_address, sender_zipcode,
        sender_city, sender_country)
        receiver_info = Receiver_Info(receiver_name, receiver_address, receiver_zipcode,
        receiver_city, receiver_country)
        try:
            id = (Order.objects.order_by('-id')[0])+1
        except Order.DoesNotExist:
           id = 1

        Order.objects.create(send_date, x_in_mm, y_in_mm, z_in_mm, is_breakable, is_perishable,
        sender_info, receiver_info, id)
        return HttpResponse("Order created succesfully")
    return render(request, 'create_order.html')

