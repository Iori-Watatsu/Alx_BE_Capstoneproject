from rest_framework import serializers
from .models import Review, Post

class ReviewSerializer (serializers.ModelSerializer):
    review_name = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source="author.username",
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'