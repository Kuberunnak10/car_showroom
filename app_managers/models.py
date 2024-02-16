from django.db import models

from app_autosalon.models import Mark


# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    permissions_cars = models.ForeignKey(Mark, on_delete=models.CASCADE)
    manager_photo = models.ImageField(upload_to='manager_photo/', null=True, blank=True)

    def __str__(self):
        return str(self.name)
