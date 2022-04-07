from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
