from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient
from category.models import Category
from products.models import Product
from cart.models import Cart, CartItem
from orders.models import Order
from reviews.models import Review
from wishlist.models import Wishlist
from django.contrib.auth import get_user_model
from products.views import ProductViewSet
from rest_framework import status
from django.urls import reverse
from django.test import TestCase

User = get_user_model()

class ProductTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='examplepasswd',
            is_staff=True
        )
        self.factory = APIRequestFactory()
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Hair Care')
        self.product = Product.objects.create(
            name="Shampoo",
            description="Hair shampoo",
            brand="BrandX",
            price=100.00,
            sale_price=90.00,
            sku="SH123",
            in_stock=50,
            is_active=True,
            is_featured=True,
            category=self.category,
        )

        self.products_url = reverse('product-list')
        self.client = APIClient()

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)

    def test_create_product_requires_auth(self):
        payload = {
            'name': 'Conditioner',
            'description': 'Hair conditioner',
            'brand': 'BrandX',
            'price': 120,
            'sale_price': 100,
            'sku': 'CO123',
            'in_stock': 20
        }
        response = self.client.post('/api/products', payload, format='json')
        self.assertEqual(response.status_code, 201)
