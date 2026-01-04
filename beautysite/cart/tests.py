from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient
from category.models import Category
from products.models import Product
from cart.models import Cart, CartItem
from orders.models import Order
from reviews.models import Review
from wishlist.models import Wishlist
from django.contrib.auth import get_user_model
from cart.views import CartItemViewSet
from django.urls import reverse


User = get_user_model()

class CartTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Hair Care")
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="cartuser", password="pass123")
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            name="Shampoo",
            description="Hair shampoo",
            brand="BrandX",
            price=100.00,
            sale_price=90.00,
            sku="SH123",
            stock=50,
            category=self.category,
        )

        self.url = reverse('cartitem-list')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_add_item_to_cart(self):
        request = self.factory.post('/api/cart/', {'product': self.product.id, 'quantity': 2})
        force_authenticate(request, user=self.user)
        response = CartItemViewSet.as_view({'post':'create'})(request)
        self.assertEqual(response.status_code, 201)

    def test_list_cart_items(self):
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)
        request = self.factory.get('/api/cart/')
        force_authenticate(request, user=self.user)
        response = CartItemViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        