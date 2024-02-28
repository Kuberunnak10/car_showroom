from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404

from app_api.serializers import AutoSerializers, MarkSerializers
from app_autosalon.models import Auto, Mark

from rest_framework.views import APIView


class AutoEndpoint(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializers
    http_method_names = ["get"]


class MarkEndpoints(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializers


class MarkList(ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializers


class MarkAPIList(RetrieveAPIView):
    serializer_class = MarkSerializers

    def get_object(self):
        mark = self.kwargs['name']
        return get_object_or_404(Mark, name=mark)



