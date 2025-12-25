from django.db import models
from users.models import CustomUser
from products.models import Product
from django.conf import settings

# Create your models here.
class Review(models.Model):
   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    title = models.CharField(max_length=100)
    comment = models.TextField()
    is_approved = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
