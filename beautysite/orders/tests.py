from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .models import Order
from .views import OrderViewSet

User = get_user_model()

class OrderTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="orderuser", password="pass123")
        self.order = Order.objects.create(user=self.user, total_price=500, status="pending")

    def test_list_orders(self):
        request = self.factory.get('/api/orders/')
        force_authenticate(request, user=self.user)
        response = OrderViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        request = self.factory.post('/api/orders/', {'total_price': 200, 'status': 'pending'})
        force_authenticate(request, user=self.user)
        response = OrderViewSet.as_view({'post':'create'})(request)
        self.assertEqual(response.status_code, 201)
        