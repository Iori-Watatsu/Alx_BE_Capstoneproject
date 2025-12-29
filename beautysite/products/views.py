from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
def products(request):
    return HttpResponse("Browse beauty products")

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    filterset_fields = ['brand']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']