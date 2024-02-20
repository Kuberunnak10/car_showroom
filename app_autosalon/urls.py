from django.urls import  path

from app_autosalon.views import index, get_mark, get_auto

urlpatterns = [
    path('', index, name='main_page'),
    path('cars/<str:mark>', get_mark, name='mark_name'),
    path('cars/sale/<int:id>', get_auto, name='get_auto')
]
