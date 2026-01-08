from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, filters, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Post, Wishlist
from .serializers import PostSerializer, WishlistSerializer
from .permissions import IsAuthorOrReadOnly
from .filters import WishlistFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PostListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filtering_class = WishlistFilter
    search_fields = ['product_name']
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]