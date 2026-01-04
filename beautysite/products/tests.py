from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status
from .models import Product
from .views import ProductViewSet

User = get_user_model()

class ProductTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="testuser", password="pass123")
        self.product = Product.objects.create(
            name="Shampoo",
            description="Hair shampoo",
            brand="BrandX",
            price=100.00,
            sale_price=90.00,
            sku="SH123",
            stock_quantity=50
        )

    def test_list_products(self):
        request = self.factory.get('/api/products/')
        response = ProductViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_create_product_requires_auth(self):
        request = self.factory.post('/api/products/', {
            'name': 'Conditioner',
            'description': 'Hair conditioner',
            'brand': 'BrandX',
            'price': 120,
            'sale_price': 100,
            'sku': 'CO123',
            'stock_quantity': 20
        })
        force_authenticate(request, user=self.user)
        response = ProductViewSet.as_view({'post':'create'})(request)
        self.assertEqual(response.status_code, 201)
