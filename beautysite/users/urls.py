from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path('templates/'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
]