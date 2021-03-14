from django import forms
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class LoginForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  username = forms.EmailField()

  class Meta:
    model = User
    fields =['username','password']