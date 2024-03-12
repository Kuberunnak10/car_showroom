from django.urls import path, include
from rest_framework import routers

from app_api.views import MarkAPIAdminUpdateDelete, MarkAPIAdminListCreate, AutoApiModelView, MarkListList, MarkAPI

# from app_api.views import MarkEndpoints

router = routers.DefaultRouter()

# View with custom permission class
router.register('auto', AutoApiModelView)


urlpatterns = [
    path('', include(router.urls)),
    path('mark_list/', MarkListList.as_view()),
    path('mark_list/<str:name>', MarkAPI.as_view()),
    path('mark_admin/', MarkAPIAdminListCreate.as_view()),
    path('mark_admin/<str:name>', MarkAPIAdminUpdateDelete.as_view()),
]
