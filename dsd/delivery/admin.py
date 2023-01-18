from django.contrib import admin

from .models import Order, Delivery, Sender_Info, Receiver_Info, Product, Price, Delivery_Driver

admin.site.register(Order)

admin.site.register(Delivery)

admin.site.register(Sender_Info)

admin.site.register(Receiver_Info)

admin.site.register(Product)

admin.site.register(Price)

admin.site.register(Delivery_Driver)