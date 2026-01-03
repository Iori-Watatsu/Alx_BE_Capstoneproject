import django_filters
from .models import Cart_Item

class CartItemFilter(django_filters.FilterSet):

    class Meta:
        model = Cart_Item
        fieldsets = {
            'product_name':['icontains'],
            'quantity':['gte', 'lte']
        }