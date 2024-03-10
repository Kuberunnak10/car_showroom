from django.urls import path, include
from rest_framework import routers

from app_api.views import MarkList, MarkAPIList, MarkAPIAdminUpdateDelete, MarkAPIAdminListCreate

# from app_api.views import MarkEndpoints

router = routers.DefaultRouter()

# View with custom permission class
# router.register('mark', MarkEndpoints)


urlpatterns = [
    # path('', include(router.urls)),
    path('mark_list/', MarkList.as_view()),
    path('mark_list/<str:name>', MarkAPIList.as_view()),
    path('mark_admin/', MarkAPIAdminListCreate.as_view()),
    path('mark_admin/<str:name>', MarkAPIAdminUpdateDelete.as_view()),
]
