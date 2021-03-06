from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Item, ShopUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["price", "name", "category"]

