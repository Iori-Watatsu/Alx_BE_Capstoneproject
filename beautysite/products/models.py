from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    parent_id = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='parent_categories', null =True, blank=True)
    is_active = models.BooleanField(default=True)

class Product(models.Model):
    id = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    brand = models.CharField(max_length=100)
    price = models.DecimalField()
    sale_price = models.DecimalField()
    sku = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    is_featured = models.BooleanField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class ProductImage(models.Model):
    id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    image_url = models.CharField(max_length=50)
    alt_text = models.TextField()
    is_primary = models.BooleanField()

