from django.db import models
class Sender_Info(models.Model):
    name = models.CharField(max_length=50)
    street_and_number: models.CharField(max_length=50)
    zipcode= models.CharField(max_length=8)
    city = models.CharField(max_length=85)
    country= models.CharField(max_length=56)

class Order(models.Model):
    question_text = models.CharField(max_length=200)
    send_date = models.DateTimeField('send date')
    x_in_mm = models.IntegerField(max_length=2000)
    y_in_mm = models.IntegerField(max_length=2000)
    z_in_mm = models.IntegerField(max_length=2000)
    is_breakable = models.BooleanField(default=False)
    is_perishable = models.BooleanField(default=False)
    sender_info = models.ForeignKey(Sender_Info, on_delete=models.CASCADE)




