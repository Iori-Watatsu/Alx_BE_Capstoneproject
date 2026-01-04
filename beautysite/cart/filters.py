import django_filters
from .models import CartItem

class CartItemFilter(django_filters.FilterSet):

    class Meta:
        model = CartItem
        fields = '__all__'