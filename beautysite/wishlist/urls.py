from django.conf.urls.i18n import urlpatterns
from django.db import router
from django.urls import path, include
from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, WishlistViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', WishlistViewSet, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail')
]