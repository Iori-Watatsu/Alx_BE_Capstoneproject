import django_filters
from .models import Review

class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = {
            'rating': ['gte', 'lte'],
            'product': ['exact']
        }
