from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app_api.views import AutoEndpoint, MarkEndpoints

router = routers.DefaultRouter()

router.register('auto', AutoEndpoint)
router.register(r'mark/(?P<auto_id>\d+)/hello/(?P<id>\d+)', MarkEndpoints)


urlpatterns = [
    path('', include(router.urls))
]
