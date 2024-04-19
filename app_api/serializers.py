from abc import ABC, abstractmethod

from rest_framework import serializers

from app_autosalon.models import Auto, Galery, Mark, Country, BodyType, Transmission, Color


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ['id', 'name_bodytype']


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ['id', 'type']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'car_color']


class GalerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = ['image', ]


class MarkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Mark
        fields = '__all__'


class AutoSerializers(serializers.ModelSerializer):
    mark_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    images = GalerySerializers(many=True, read_only=True)

    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    def get_username(self, obj):
        return obj.user.username

    def get_mark_name(self, obj):
        return obj.mark.name

    class Meta:
        model = Auto
        fields = ['mark', 'mark_name', 'images', 'model', 'country', 'body_type', 'price', 'transmission', 'power',
                  'color', 'user', 'username']
