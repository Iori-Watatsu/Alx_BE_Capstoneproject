from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post, Cart_Item
from .serializers import PostSerializer, CartItemSerializer
from .permissions import IsAuthorOrReadOnly
from .filters import CartItemFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def cart(request):
    return HttpResponse("What's in your cart")

def perform_create(self, serializer):
    serializer.save(user=self.request.user)
    
class PostListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = [PostSerializer]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostReviewUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = [PostSerializer]
    queryset = Post.objects.all()

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = CartItemFilter
    search_fields = ['product_name']
    ordering_fields = ['quantity', 'created_at']

    def get_queryset(self):
        return Cart_Item.objects.filter(user=self.request.user)