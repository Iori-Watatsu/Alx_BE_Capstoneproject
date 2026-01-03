from rest_framework import serializers
from .models import Review

class ReviewSerializer (serializers.ModelSerializer):
    review_name = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = [
            'id',
            'rating',
            'comment',
            'user',
            'review_name',
            'created_at',
        ]