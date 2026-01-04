from django.urls import path
from .views import (PostListCreateAPIView, PostReviewUpdateDestroyAPIView)
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'items', CartItemViewSet, basename='cartitem')
router.register(r'', CartViewSet, basename='cart')

urlpatterns = router.urls

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk/', PostReviewUpdateDestroyAPIView.as_view(),)
]