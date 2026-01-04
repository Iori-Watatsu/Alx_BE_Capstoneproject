
from django.urls import path
from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, ReviewViewSet )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='review')

urlpatterns = router.urls

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
]
