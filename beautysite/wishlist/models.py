from django.db import models

# Create your models here.
class Wishlist(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    added_at = models.DateTimeField()
    