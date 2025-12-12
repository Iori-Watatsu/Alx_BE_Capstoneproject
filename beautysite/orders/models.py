from django.db import models
from django.db.models import TextField, CASCADE
from products.models import products
from users.models import Profile

# Create your models here.
class Order(models.Model):
    id = models.IntegerField()
    order_number = models.CharField(max_length=100)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='users')
    total_amount = models.DecimalField()
    status = models.TextField()
    shipping_address = models.TextField()
    billing_address = models.TextField()
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Order_Item(models.Model):
    id = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=CASCADE, related_name='orders')
    product_id = models.ForeignKey(Product, on_delete=CASCADE, related_name='products')
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField()
    subtotal = models.DecimalField()