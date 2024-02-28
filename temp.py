import os
import django
from app_autosalon.models import Auto

# Указать путь к файлу settings.py в переменной окружения
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


# auto = Auto.objects.all()
#
# print(auto)
