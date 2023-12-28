from django.db import models

# Create your models here.
class Transaksi(models.Model):
    order_no = models.CharField(max_length=100)
    item_name = models.CharField(max_length=150)
    order_time = models.DateTimeField()
    ccustomer = models.CharField(max_length=100)
    qty = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    price = models.CharField(max_length=150)