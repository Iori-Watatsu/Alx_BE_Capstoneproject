from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from category.models import Category
from products.models import Product
from cart.models import Cart, CartItem
from orders.models import Order
from reviews.models import Review
from wishlist.models import Wishlist
from users.models import User

User = get_user_model()

class ReviewTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Hair Care")
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="reviewer", password="pass123")
        self.product = Product.objects.create(
            name="Conditioner",
            description="Hair conditioner",
            brand="BrandX",
            price=120.00,
            sale_price=100.00,
            sku="CO123",
            stock_quantity=20,
            is_active=False,
            is_featured=True,
            category=self.category,
        )
        self.review = Review.objects.create(user=self.user, product=self.product, rating=5, comment="Great!")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_review(self):
        request = self.factory.post('/api/reviews/', {'product': self.product.id, 'rating': 4, 'comment': 'Nice!'})
        force_authenticate(request, user=self.user)
        response = ReviewViewSet.as_view({'post':'create'})(request)
        self.assertEqual(response.status_code, 201)

    def test_list_reviews(self):
        request = self.factory.get('/api/reviews/')
        response = ReviewViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)
        