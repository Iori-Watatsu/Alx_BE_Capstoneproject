from rest_framework import serializers
from .models import Cart, CartItem, Post


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'quantity',
        ]

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source='author.useranme',
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author_username',
            'created_at',
        ]