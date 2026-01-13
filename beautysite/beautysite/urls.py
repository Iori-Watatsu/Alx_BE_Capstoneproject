"""
URL configuration for beautysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from users.views import SignUpView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/wishlist/', include('wishlist.urls')),
    path('api/category/', include('category.urls')),

    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile',
         TemplateView.as_view(template_name='auth/../templates/profile.html'),
         name='profile'),
    path("signup/", SignUpView.as_view(), name="signup"),

    # api views
    path('api/', include('products.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
    path('auth/', include('rest_framework_social_oauth2.urls')),

    # Authentication URLs
    path('auth/login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('auth/signup/', views.signup, name='signup'),
    path('auth/change-password/', auth_views.PasswordChangeView.as_view(
             template_name='auth/change_password.html',
             success_url='/auth/password-changed/'
         ), name='change_password'),
    path('auth/password-changed/', auth_views.PasswordChangeDoneView.as_view(
             template_name='auth/password_changed.html'
         ), name='password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)