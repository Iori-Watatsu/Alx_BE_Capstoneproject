from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient
from .models import Order
from .views import OrderViewSet
from cart.models import Cart, CartItem
from category.models import Category
from products.models import Product

User = get_user_model()

class OrderTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="orderuser", password="pass123")
        self.order = Order.objects.create(user=self.user, total_price=500, status="pending")

        self.category = Category.objects.create(name="Hair Care")
        self.product = Product.objects.create(
            name="Shampoo",
            description="Hair shampoo",
            price=100,
            stock=50,
            category=self.category
        )
        
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)


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
        