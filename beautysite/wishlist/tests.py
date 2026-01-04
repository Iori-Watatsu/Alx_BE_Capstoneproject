from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .models import Wishlist
from .views import WishlistViewSet
from products.models import Product

User = get_user_model()

class WishlistTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Hair Care")
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="wishlistuser", password="pass123")
        self.product = Product.objects.create(
            name="Body Lotion",
            description="Moisturizing lotion",
            brand="BrandY",
            price=150.00,
            sale_price=120.00,
            sku="BL123",
            stock_quantity=30,
            is_active=False,
            is_featured=True,
            category=self.category
        )

    def test_add_to_wishlist(self):
        request = self.factory.post('/api/wishlist/', {'product': self.product.id})
        force_authenticate(request, user=self.user)
        response = WishlistViewSet.as_view({'post':'create'})(request)
        self.assertEqual(response.status_code, 201)

    def test_list_wishlist_items(self):
        Wishlist.objects.create(user=self.user, product=self.product)
        request = self.factory.get('/api/wishlist/')
        force_authenticate(request, user=self.user)
        response = WishlistViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
