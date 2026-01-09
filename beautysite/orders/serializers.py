from rest_framework import serializers
from .models import Post, Order, OrderItem
from products.models import Product
from cart.models import CartItem

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

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validate_data):
        validate_data['total_price'] = validate_data.get('total_price', 0)
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validate_data)
        cart = validate_data.get('cart', None)
        if cart_id:
            cart_items = CartItem.objects.filter(cart_id=cart_id)
            total_price = 0
            for item in cart.cartitem_set.all():
                OrderItem.objects.create(
                    order = order,
                    product = item.product,
                    quantity = item.quantity,
                    price = item.product.sale_price
                )
                total_price += item.quantity * item.product.sale_price
                order.total_price = total_price
                order.save()
        return order

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
