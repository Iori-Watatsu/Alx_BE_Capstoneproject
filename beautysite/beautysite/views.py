# beautysite/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    """Home page view"""
    return render(request, 'index.html')

@login_required
def profile(request):
    """User profile view"""
    return render(request, 'profile.html')

def signup(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log the user in after signup
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})

# Simple views for other pages
def shop(request):
    return render(request, 'shop.html')

def cart(request):
    return render(request, 'cart.html')


def csrf_failure(request, reason=""):
    return render(request, "csrf_failure.html", status=403)