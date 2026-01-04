from django.db import models
from django.template.context_processors import request

from users.models import Profile, CustomUser
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Cart(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart({self.user})"

class CartItem(models.Model):

    cart = models.ForeignKey(
        'cart.Cart',
        on_delete=models.CASCADE, null=True, blank=True
    )
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} x {self.quantity}"

    class Meta:
        unique_together = ('cart', 'product')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# alias for model name change for testing
Cart_Item = CartItem