from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    #id = models.IntegerField()
    #username = models.CharField(max_length=15)
    #email = models.EmailField()
    #password = models.CharField(max_length=50)
    #first_name = models.TextField()
    #last_name = models.TextField()
    phone_number = models.CharField(max_length=255, blank=True)
    #date_joined = models.DateTimeField()
    #is_active = models.BooleanField()
    #is_staff = models.BooleanField()
    #is_superuser = models.BooleanField()


class Profile(models.Model):
    id = models.IntegerField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profile')
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
    created_at = models.DateTimeField(auto_now=True)
