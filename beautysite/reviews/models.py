from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Review(models.Model):
    id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    rating = models.IntegerField()
    title = models.CharField(max_length=100)
    comment = models.TextField()
    is_approved = models.BooleanField()
    created_at = models.DateTimeField()
