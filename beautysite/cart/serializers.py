from rest_framework import serializers
from .models import Cart, CartItem, Post
from products.serializers import ProductSerializer
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['cart']

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source='author.useranme',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
