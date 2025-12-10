from django.db import models

# Create your models here.
class Review(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    rating = models.IntegerField()
    title = models.CharField(max_length=100)
    comment = models.TextField()
    is_approved = models.BooleanField()
    created_at = models.DateTimeField()
