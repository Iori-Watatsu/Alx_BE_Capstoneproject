from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    category_id = models.IntegerField()
    brand = models.CharField(max_length=100)
    price = models.DecimalField()
    sale_price = models.DecimalField()
    sku = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    is_featured = models.BooleanField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
