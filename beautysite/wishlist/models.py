from django.db import models
from users.models import Profile
from products.models import Product

# Create your models here.
class Wishlist(models.Model):
    id = models.IntegerField()
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    added_at = models.DateTimeField()
    