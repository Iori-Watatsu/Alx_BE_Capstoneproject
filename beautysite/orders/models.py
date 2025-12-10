from django.db import models
from django.db.models import TextField


# Create your models here.
class Order(models.Model):
    id = models.IntegerField()
    order_number = models.CharField(max_length=100)
    user_id = models.IntegerField()
    total_amount = models.DecimalField()
    status = models.TextField()
    shipping_address = models.TextField()
    billing_address = models.TextField()
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()