from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app_api.views import AutoEndpoint, MarkEndpoints, MarkList, MarkAPIList

router = routers.DefaultRouter()

router.register('auto', AutoEndpoint)
router.register('mark', MarkEndpoints)
# router.register('list', MarkEnd)


urlpatterns = [
    path('', include(router.urls)),
    path('mark_list', MarkList.as_view()),
    path('mark_list/<str:name>', MarkAPIList.as_view())
]
