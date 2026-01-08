from django.urls import path, include
from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView)
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListCreateAPIView.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='post-detail'),
]