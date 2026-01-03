from django.db import models
from users.models import Profile
from products.models import Product
from django.conf import settings

# Create your models here.
class Wishlist(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='whishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
