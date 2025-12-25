from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DetailView
from .models import CustomUser, UserProfile
from .forms import CustomUserCreationForm, ProfileUpdateForm

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def users(request):
    return HttpResponse("Welcome, User")

class UserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)

            UserProfile.objects.create(user=user)

class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'