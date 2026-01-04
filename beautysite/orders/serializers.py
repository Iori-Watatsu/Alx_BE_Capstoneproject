from rest_framework import serializers
from .models import Post, Order

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source="author.username",
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


class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = [
            'total_price'
        ]

    def create(self, validate_data):
        validate_data['total_price'] = validate_data.get('total_price', 0)
        return super().create(validate_data)