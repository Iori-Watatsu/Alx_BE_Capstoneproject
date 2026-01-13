from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DetailView
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, ProfileUpdateForm
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def profile(request):
    return render(request, 'users/profile.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/../templates/accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)

            Profile.objects.create(user=user)

        return response

class CustomLoginView(LoginView):
    template_name = 'registration/../templates/accounts/login.html'
    redirect_authenticated_user = True

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate credentials

        # Login user

        return Response("user logged in")

@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'auth/../templates/profile.html', {
        'user': user,
        'profile': profile
    })

@login_required
def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()

        profile.skin_type = request.POST.get('skin_type', profile.skin_type)
        profile.skin_concerns = request.POST.get('skin_concerns', profile.skin_concerns)
        profile.save()

        return redirect('profile')

    return render(request, 'users/edit_profile.html', {
        'user': user,
        'profile': profile
    })


@login_required
def beauty_quiz(request):
    if request.method == 'POST':
        profile, created = Profile.objects.get_or_create(user=request.user)

        profile.skin_type = request.POST.get('skin_type', '')
        profile.skin_concerns = request.POST.get('skin_concerns', '')
        profile.preferred_brands = request.POST.get('preferred_brands', '')
        profile.allergies = request.POST.get('allergies', '')
        profile.save()

        return redirect('profile')

    return render(request, 'users/beauty_quiz.html')

class CustomLogoutView(APIView):
    def post(self, request):
        # Logout user

        return Response("user logged out")