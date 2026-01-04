import django_filters
from .models import  Order

class OrderFilter(django_filters.FilterSet):

    created_at_gte = django_filters.DateTimeFilter(
        field_name='created_at', lookup_expr='gte'
    )
    created_at_lte = django_filters.DateTimeFilter(
        field_name='created_at', lookup_expr='lte'
    )

    class Meta:
        model = Order
        fields = ['created_at_gte', 'created_at_lte']