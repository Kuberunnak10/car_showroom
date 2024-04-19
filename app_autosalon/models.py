from django.contrib.auth.models import User
from django.db import models


class Mark(models.Model):
    name = models.CharField(max_length=255, unique=True)
    car_image = models.ImageField(upload_to='makr_image/', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Transmission(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return str(self.type)


class Color(models.Model):
    car_color = models.CharField(max_length=255)

    def __str__(self):
        return str(self.car_color)


class BodyType(models.Model):
    name_bodytype = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name_bodytype)


class Auto(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    price = models.IntegerField()
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    power = models.FloatField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(f'{self.mark}, {self.model}')


class Galery(models.Model):
    image = models.ImageField(upload_to='car_photo')
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(f'{self.auto}')



