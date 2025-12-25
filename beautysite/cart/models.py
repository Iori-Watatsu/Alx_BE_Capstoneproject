from django.db import models
from products.models import Product
from users.models import Profile

# Create your models here.
class Cart(models.Model):
    
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Cart_Item(models.Model):

    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    added_at = models.DateTimeField()