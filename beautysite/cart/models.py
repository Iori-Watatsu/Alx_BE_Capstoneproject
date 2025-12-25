from django.db import models
from products.models import Product
from users.models import Profile
from django.conf import settings

# Create your models here.
class Cart(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Cart_Item(models.Model):

    cart_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    added_at = models.DateTimeField()