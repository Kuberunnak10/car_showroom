from django.urls import path

from app_course.views import exchange

urlpatterns = [
    path('', exchange, name='course'),
]
