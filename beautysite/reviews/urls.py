from django.urls import path
from django.urls import path
from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
]
