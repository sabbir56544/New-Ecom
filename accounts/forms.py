from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

