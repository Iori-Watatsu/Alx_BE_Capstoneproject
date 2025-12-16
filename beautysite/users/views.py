from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Profile

# Create your views here.
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
    form_class = UserCreationForm
    template_name = '/beautysite/templates/registration/signup.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()

        Profile.objects.create(user=user)

        login(self.request, user)

        return redirect('profile')