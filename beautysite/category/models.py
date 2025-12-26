from django.db import models

# Create your models here.
class Category(models.Model):
   
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null =True, blank=True)
    is_active = models.BooleanField(default=True)