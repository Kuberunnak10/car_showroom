from django.urls import path

from app_news.views import get_news

urlpatterns = [
    path('', get_news, name='news')
    ]