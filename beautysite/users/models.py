from django.db import models

# Create your models here.
id = models.IntegerField()
usename = models.CharField(max_length=15)
email = models.EmailField()
password = models.CharField(min_length=16, max_length=50)
first_name = models.TextField()
last_name = models.TextField()
phone_number = models.IntegerField()
date_joined = models.DateTimeField()
is_active = models.BooleanField()
is_staff = models.BooleanField()
is_superuser = models.BooleanField()
