from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post, Wishlist
from .serializers import PostSerializer, WishlistSerializer
from .permissions import IsAuthorOrReadOnly
from .filters import WishlistFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def wishlist(request):
    return HttpResponse("Your wishes")

class PostListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

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