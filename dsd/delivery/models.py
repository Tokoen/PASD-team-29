from django.db import models

class Sender_Info(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    street_and_number=models.CharField(max_length=50)
    zipcode= models.CharField(max_length=8)
    city = models.CharField(max_length=85)
    country= models.CharField(max_length=56)

class Receiver_Info(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    street_and_number= models.CharField(max_length=50)
    zipcode= models.CharField(max_length=8)
    city = models.CharField(max_length=85)
    country= models.CharField(max_length=56)

class Order(models.Model):
    send_date = models.DateField('send date')
    x_in_mm = models.IntegerField()
    y_in_mm = models.IntegerField()
    z_in_mm = models.IntegerField()
    is_breakable = models.BooleanField()
    is_perishable = models.BooleanField()
    sender_info = models.ForeignKey(Sender_Info, on_delete=models.CASCADE)
    receiver_info = models.ForeignKey(Receiver_Info, on_delete=models.CASCADE)
    id = models.IntegerField(unique=True, primary_key=True)

class Delivery(models.Model):
    expected_delivery_datetime = models.DateTimeField('expected delivery date')
    actual_delivery_datetime = models.DateTimeField('actual delivery date')
    order_id = models.IntegerField(unique=True)
    cost_in_cents = models.IntegerField()
    status = models.CharField(max_length=10)
    id = models.IntegerField(unique=True, primary_key=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)








