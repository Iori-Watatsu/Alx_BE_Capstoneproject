from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, filters, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post, CartItem, Cart
from .serializers import PostSerializer, CartItemSerializer, CartSerializer
from .permissions import IsAuthorOrReadOnly
from .filters import CartItemFilter
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Product
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
def cart(request):
    return HttpResponse("What's in your cart")
    
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
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = CartItemFilter
    search_fields = ['product_name']
    ordering_fields = ['quantity', 'created_at']

    def get_queryset(self):
        cart = Cart.objects.get_or_create(user=self.request.user)[0]
        return CartItem.objects.filter(idt=cart.id)

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart.id)

    def get_object(self):

        cart = Cart.objects.get_or_create(user=self.request.user)
        return cart
