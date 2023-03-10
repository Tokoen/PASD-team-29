# Generated by Django 4.1.5 on 2023-01-17 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('expected_delivery_datetime', models.DateTimeField(verbose_name='expected delivery date')),
                ('actual_delivery_datetime', models.DateTimeField(verbose_name='actual delivery date')),
                ('order_id', models.IntegerField(unique=True)),
                ('cost_in_cents', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receiver_Info',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('street_and_number', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=85)),
                ('country', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Sender_Info',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('street_and_number', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=85)),
                ('country', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('send_date', models.DateField(verbose_name='send date')),
                ('x_in_mm', models.IntegerField()),
                ('y_in_mm', models.IntegerField()),
                ('z_in_mm', models.IntegerField()),
                ('is_breakable', models.BooleanField()),
                ('is_perishable', models.BooleanField()),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('receiver_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delivery.receiver_info')),
                ('sender_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delivery.sender_info')),
            ],
        ),
    ]
