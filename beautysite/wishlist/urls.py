from django.conf.urls.i18n import urlpatterns
from django.db import router
from django.urls import path
from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, WishlistViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', WishlistViewSet, basename='wishlist')

urlpatterns = router.urls