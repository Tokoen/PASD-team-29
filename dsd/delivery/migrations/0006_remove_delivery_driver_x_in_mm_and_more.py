# Generated by Django 4.1.5 on 2023-01-18 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_delivery_driver_deliveries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery_driver',
            name='x_in_mm',
        ),
        migrations.RemoveField(
            model_name='delivery_driver',
            name='y_in_mm',
        ),
        migrations.RemoveField(
            model_name='delivery_driver',
            name='z_in_mm',
        ),
    ]
