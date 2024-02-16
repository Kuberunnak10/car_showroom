from rest_framework import serializers

from app_autosalon.models import Auto, Galery, Mark


class GalerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = ['image',]


class AutoSerializers(serializers.ModelSerializer):
    images = GalerySerializers(many=True, read_only=True)

    class Meta:
        model = Auto
        fields = ['mark', 'model', 'country', 'body_type', 'price', 'images',]


class MarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['name', 'car_image']




