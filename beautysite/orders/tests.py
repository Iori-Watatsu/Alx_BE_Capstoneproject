from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient
from .models import Order
from .views import OrderViewSet
from cart.models import Cart, CartItem
from category.models import Category
from products.models import Product
from django.urls import reverse

User = get_user_model()

class OrderTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="orderuser", password="pass123", email='test@example.com')
        self.order = Order.objects.create(user=self.user, total_price=500, status="pending")

        self.category = Category.objects.create(name="Hair Care")
        self.product = Product.objects.create(
            name="Shampoo",
            description="Hair shampoo",
            sale_price=90.00,
            price=100,
            stock_quantity=50,
            category=self.category
        )
        
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = reverse('order-list')

    def test_list_orders(self):
        request = self.factory.get('/api/orders/')
        force_authenticate(request, user=self.user)
        response = OrderViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        payload = {
            "cart_id": self.cart.id,
            "shipping_address": "123 Main St",
            "payment_method": "card"
        }
        request = self.factory.post('/api/orders/', {'total_price': 200, 'status': 'pending'})
        force_authenticate(request, user=self.user)
        response = self.client.post("/api/orders/", payload, format='json')
        self.assertEqual(response.status_code, 201)
        