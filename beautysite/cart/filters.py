import django_filters
from .models import CartItem

class CartItemFilter(django_filters.FilterSet):

    class Meta:
        model = CartItem
        fieldsets = {
            'product_name':['icontains'],
            'quantity':['gte', 'lte']
        }