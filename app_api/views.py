from django.shortcuts import render
from rest_framework import viewsets

from app_api.serializers import AutoSerializers, MarkSerializers
from app_autosalon.models import Auto, Mark


class AutoEndpoint(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializers
    http_method_names = ["get"]


class MarkEndpoints(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializers



