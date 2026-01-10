from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'brand', 'price', 'is_on_sale',
            'sale_price', 'sku', 'in_stock', 'category', 'category_id',
            'is_active', 'is_featured',
        ]
        read_only_fields = [
            'id', 'name', 'description', 'brand', 
            'sale_price', 'sku', 'category',
            'is_active', 'is_featured',
        ]

    def validate_price(self, value):
        if value <= 0 : # \eqslantless sign was automatically created when adding the = sign next to the <
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    def validate(self, data):
        sale_price = data.get('sale_price')
        price = data.get('price')

        if sale_price and sale_price >= price: # \eqslantgtr sign was automatically created when adding the = sign next to the >
            raise serializers.ValidationError("Sale price must be less than regular price.")
        return data

    def get_is_on_sale(self, obj):
        if obj.sale_price is None:
            return False
        return obj.sale_price < obj.price


