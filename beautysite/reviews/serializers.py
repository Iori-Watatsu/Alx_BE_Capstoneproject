from rest_framework import serializers
from .models import Review, Post
from products.models import Product
class ReviewSerializer (serializers.ModelSerializer):
    review_name = serializers.CharField(
        source='user.username',
        read_only=True
    )

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    class Meta:
        model = Review
        fields = [
            'id',
            'product',
            'rating',
            'comment',
            'user',
            'review_name',
            'created_at',
        ]
        read_only_fields = ['created_at']

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source="author.username",
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'