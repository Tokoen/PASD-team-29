from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

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
    if request.POST.get('send_date'):
        send_date = request.POST.get('send_date')
        x_in_mm = request.POST.get('x_in_mm')
        y_in_mm = request.POST.get('y_in_mm')
        z_in_mm = request.POST.get('z_in_mm')
        is_breakable = request.POST.get('is_breakable')
        is_perishable = request.POST.get('is_perishable')
        sender_name = request.POST.get('sender_name')
        sender_address = request.POST.get('sender_address')
        sender_zipcode = request.POST.get('sender_zipcode')
        sender_city = request.POST.get('sender_city')
        sender_country = request.POST.get('sender_country')
        receiver_name = request.POST.get('receiver_name')
        receiver_address = request.POST.get('receiver_address')
        receiver_zipcode = request.POST.get('receiver_zipcode')
        receiver_city = request.POST.get('receiver_city')
        receiver_country = request.POST.get('receiver_country')

        sender_info = Sender_Info(sender_name, sender_address, sender_zipcode,
        sender_city, sender_country)
        if Sender_Info.DoesNotExist:
            sender_info.save()

        receiver_info = Receiver_Info(receiver_name, receiver_address, receiver_zipcode,
        receiver_city, receiver_country)
        if Sender_Info.DoesNotExist:
            receiver_info.save()

        if Order.DoesNotExist:
            id = 1
        else:
            id = (Order.objects.last().id)+1

        order = Order(send_date, x_in_mm, y_in_mm, z_in_mm, is_breakable, is_perishable, sender_info.name, receiver_info.name, id)

        order.save()
        return HttpResponseRedirect("/delivery/checkout")

    return render(request, 'create_order.html')

def create_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': Price.objects.last().stripe_price_id,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url="https://www.soroptimistindianrock.org/wp-content/uploads/2021/01/PAYMENT-SUCCESS.png",
        cancel_url="https://renewsat.com/wp-content/uploads/2022/01/Paymentfailedforweb.png",
    )
    return HttpResponseRedirect(session.url)



