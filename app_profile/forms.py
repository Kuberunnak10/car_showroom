from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app_profile.models import BookingModel


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ['first_name', 'last_name', 'number_phone', 'email', 'interesting_car']
