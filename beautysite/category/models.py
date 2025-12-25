from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    parent_id = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='parent_categories', null =True, blank=True)
    is_active = models.BooleanField(default=True)