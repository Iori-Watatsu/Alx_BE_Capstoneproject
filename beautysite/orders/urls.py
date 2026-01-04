from django.urls import path
from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView)
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = router.urls

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
]