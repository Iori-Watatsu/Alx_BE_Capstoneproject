from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

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
