from django.urls import path

from app_profile.views import registration, profile

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    ]
