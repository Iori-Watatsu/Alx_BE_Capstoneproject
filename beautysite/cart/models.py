from django.db import models

# Create your models here.
class Cart(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()