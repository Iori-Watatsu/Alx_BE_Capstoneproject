import django_filters
from .models import  Order

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            'status':['exact'],
            'total_price':['gte', 'lte'],
            'created_at':['date', 'date_gte', 'date_lte']
        }