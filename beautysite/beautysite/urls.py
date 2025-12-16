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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('templates/', include('django.contrib.auth.urls')),
    path('templates/accounts/',TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('templates/change_passwd',TemplateView.as_view(template_name='passwd_reset/change_passwd.html'), name='change_passwd'),
    path('templates/passwd_changed/',TemplateView.as_view(template_name='passwd_reset/passwd_changed.html'), name='passwd_changed'),
    path('templates/registration/,TemplateView.as_view(template_name='registration/login.html', name=),
    path('templates/registration',TemplateView.as_view(template_name='registration/login.html'), name='login'),
         path('accounts/', include('django.contrib.auth.urls')),
]
