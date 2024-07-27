from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    serial = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    alternative_phone = models.CharField(max_length=11, blank=True, null=True)
    governorate = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    address = models.TextField()
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
