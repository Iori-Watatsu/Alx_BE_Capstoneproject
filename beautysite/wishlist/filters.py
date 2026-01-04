import django_filters
from .models import Wishlist

class WishlistFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name='product', lookup_expr='icontains')

    class Meta:
        model = Wishlist
        fields = ['product']