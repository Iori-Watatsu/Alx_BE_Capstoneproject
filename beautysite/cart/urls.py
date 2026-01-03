from django.urls import path
from .views import (PostListCreateAPIView, PostReviewUpdateDestroyAPIView)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk/', PostReviewUpdateDestroyAPIView.as_view(),)
]