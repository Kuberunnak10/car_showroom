from django.urls import path

from app_managers.views import get_managers

urlpatterns = [
    path('', get_managers, name='get_managers')
    ]