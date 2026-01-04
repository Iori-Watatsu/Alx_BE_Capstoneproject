from rest_framework import serializers
from .models import Post, Wishlist
from products.models import Product
from wishlist.views import WishlistViewSet

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

class ProductMiniSerializer(serializers.ModelSerializer):

    # small serializer for wishlist

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
        ]

class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    product_details = ProductMiniSerializer(source='product', read_only=True)

    class Meta:
        model = Wishlist
        fields = [
            'id',
            'user',
            'product',
            'product_details',
            'created_at',
        ]
        read_only_fields = ['created_at']

    def validate(self, data):

        user = self.context['request'].user
        product = data.get('product')

        if WishlistItem.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError(
                "This product is already in your wishlist."
            )

        return data

