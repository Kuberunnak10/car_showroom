from rest_framework import serializers

from app_autosalon.models import Auto, Galery, Mark


class GalerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = ['image',]


class AutoSerializers(serializers.ModelSerializer):
    images = GalerySerializers(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    mark = serializers.CharField(source='mark.name')
    country = serializers.CharField(source='country.name')
    body_type = serializers.CharField(source='body_type.name_bodytype')
    transmission = serializers.CharField(source='transmission.type')
    color = serializers.CharField(source='color.car_color')

    class Meta:
        model = Auto
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Mark
        fields = '__all__'

