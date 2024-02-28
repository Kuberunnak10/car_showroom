from django.db import models


class BookingModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number_phone = models.CharField(max_length=100)
    email = models.EmailField()
    interesting_car = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
