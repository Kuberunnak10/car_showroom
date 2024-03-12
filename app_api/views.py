from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser

from app_api.permissions import IsAdminOrReadOnly
from app_api.serializers import AutoSerializers, MarkSerializer
from app_autosalon.models import Mark, Auto

# class MarkEndpoints(viewsets.ModelViewSet):
"""View with custom permission class"""
#     queryset = Mark.objects.all()
#     serializer_class = MarkSerializer
#     permission_classes = (IsAdminOrReadOnly,)


class MarkListList(generics.ListAPIView):
    """Api for all users (Read)"""
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = (AllowAny,)


class MarkAPI(generics.RetrieveAPIView):
    """Api for all users (Read) Viewing an individual mark"""
    serializer_class = MarkSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        mark = self.kwargs['name']
        return get_object_or_404(Mark, name=mark)


class MarkAPIAdminUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """Api for Admin (Read, Update, Delete)"""
    serializer_class = MarkSerializer
    permission_classes = (IsAdminUser,)

    def get_object(self):
        mark = self.kwargs['name']
        return get_object_or_404(Mark, name=mark)


class MarkAPIAdminListCreate(generics.ListCreateAPIView):
    """Api for Admin (Read, Create)"""
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = (IsAdminUser,)


class AutoApiModelView(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializers
    permission_classes = (IsAdminOrReadOnly,)
