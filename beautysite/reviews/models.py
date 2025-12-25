from django.db import models
from users.models import CustomUser
from products.models import Product
from django.conf import settings

# Create your models here.
class Review(models.Model):
    id = models.IntegerField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    rating = models.IntegerField()
    title = models.CharField(max_length=100)
    comment = models.TextField()
    is_approved = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
