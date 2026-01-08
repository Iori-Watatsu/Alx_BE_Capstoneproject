from django.urls import path, include
from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView)
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
]