from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Product

# Create your models here.
class CustomUser(AbstractUser):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.CharField(max_length=255, blank=True)
    date_joined = models.DateTimeField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar_url = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, blank=True, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ])
    skin_type = models.CharField(max_length=50, blank=True, choices=[
        ('oily', 'Oily'),
        ('dry', 'Dry'),
        ('combination', 'Combination'),
        ('normal', 'Normal'),
        ('sensitive', 'Sensitive'),
    ])
    hair_type = models.CharField(max_length=50, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    name = models.CharField(max_length=255, default="Default name")
    description = models.CharField(max_length=255, default="Default description")
    brand = models.CharField(max_length=100, default='Unknown')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sku = models.CharField(max_length=100, default="SKU-DEFAULT")
    stock_quantity = models.IntegerField(default=0)

    class Meta:
        permissions = [
            ("can_publish_post", "Can publish post")
        ]
