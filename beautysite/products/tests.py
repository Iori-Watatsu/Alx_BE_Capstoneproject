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
        self.category = Category.objects.create(name='Hair Care')
        self.factory = APIRequestFactory()
        self.user.is_staff = True
        self.user.save()
        self.product = Product.objects.create(
            name="Shampoo",
            description="Hair shampoo",
            brand="BrandX",
            price=100.00,
            sale_price=90.00,
            sku="SH123",
            in_stock=50,
            is_active=False,
            is_featured=True,
            category=self.category,
        )

        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpass123',
            email='admin@example.com'
        )

        self.url = reverse('review-list')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

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
            'stock': 20
        })
        force_authenticate(request, user=self.user)
        response = ProductViewSet.as_view({'post':'create'})(request)
        self.assertEqual(response.status_code, 201)
