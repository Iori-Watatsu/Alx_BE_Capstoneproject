from django.http import HttpResponse
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter

# Create your views here.
def products(request):
    return HttpResponse("Browse beauty products")

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at', 'price', 'name']
    ordering = ['created_at']