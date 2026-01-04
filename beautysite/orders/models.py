from django.db import models
from django.db.models import TextField, CASCADE
from products.models import Product
from users.models import Profile, CustomUser
from django.conf import settings
from django.contrib.auth.models import  User

# Create your models here.
class Order(models.Model):
    order_status = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    order_number = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=order_status,
        default="pending"
    )
    shipping_address = models.TextField()
    billing_address = models.TextField()
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):

    order_id = models.ForeignKey(Order, on_delete=CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="order_posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
