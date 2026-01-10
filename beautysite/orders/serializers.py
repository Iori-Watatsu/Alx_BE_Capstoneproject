from rest_framework import serializers
from .models import Post, Order, OrderItem
from products.models import Product
from cart.models import CartItem
import uuid

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source="author.username",
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    cart_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'cart_id',
            'shipping_address',
            'billing_address',
            'payment_method',
            'total_price',
            'status',
            'created_at',
            'user_email',
        ]
        read_only_fields = ['total_price', 'status', 'created_at']

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        cart_id = validated_data.pop('cart_id', None)
        cart_items = CartItem.objects.filter(cart_id=cart_id)


        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty.")

        order = Order.objects.create(
            user=user,
            order_number=str(uuid.uuid4()),
            payment_status='pending',
            status='pending',
            total_price=0,
            **validated_data
        )

        total_price = 0

        for item in cart_items:
            subtotal = item.quantity * item.product.sale_price

            OrderItem.objects.create(
                order = order,
                product = item.product,
            quantity = item.quantity,
                price_at_purchase = item.product.sale_price,
                subtotal = subtotal
            )

            total_price += subtotal

        order.total_price = total_price
        order.save()
        return order

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
