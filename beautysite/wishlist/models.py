from django.db import models
from users.models import Profile
from products.models import Product
from django.conf import settings

# Create your models here.
class Wishlist(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='whishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted')
    added_at = models.DateTimeField()
    