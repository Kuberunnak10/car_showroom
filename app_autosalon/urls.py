from django.urls import  path

from app_autosalon.views import index, get_mark_name, mark

urlpatterns = [
    path('', index, name='main_page'),
    path('cars/<str:mark>', get_mark_name, name='mark_name'),
    path('mark', mark),
]