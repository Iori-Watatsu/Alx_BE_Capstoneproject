from django.db import models
from products.models import Product

# Create your models here.
class Cart(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Cart_Item(models.Model):
    id = models.IntegerField()
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    added_at = models.DateTimeField()