import requests
from django.shortcuts import render
import time

from app_course.models import Course


# Create your views here.
def get_course(request):

    json_data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    valuta = json_data['base']
    json_data = 1 / json_data['rates']['USD']
    currency = round(json_data, 2)
    data = Course(name=valuta, currency=currency)
    data.save()
    return render(request, 'course/course.html', {'data': currency,})

