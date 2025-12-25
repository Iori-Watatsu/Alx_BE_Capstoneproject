from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False, max_length=30)
    last_name = forms.CharField(required=False, max_length=30)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "avatar_url",
            "date_of_birth",
            "gender",
            "skin_type",
            "hair_type",
            "address",
            "city",
            "country",
            "postal_code",
        ]
        #widgets = {
            #'skin_concerns': forms.Textarea(attrs={'rows': 3}),
            #'preferred_brands': forms.Textarea(attrs={'rows': 3}),
            #'allergies': forms.Textarea(attrs={'rows': 3}),
        #}

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']