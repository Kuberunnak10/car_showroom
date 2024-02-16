from django.urls import path

from app_profile.views import registration

urlpatterns = [
    path('registration/', registration, name='registration'),
    ]
