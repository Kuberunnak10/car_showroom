from django.urls import path

from app_course.views import get_course

urlpatterns = [
    path('', get_course, name='course')
]