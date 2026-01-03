from rest_framework import serializers
from .models import Cart, Cart_Item


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Item
        fields = [
            'id',
            'product',
            'quantity',
        ]

