import requests
import pickle

from celery import shared_task
from django.conf import settings
import datetime

api = settings.API_KEY_NEWS

now = datetime.date.today()
yesterday = now - datetime.timedelta(days=1)


@shared_task
def get_news():
    news = requests.get(
        f'https://newsapi.org/v2/everything?q=auto&from={yesterday}&sortBy=publishedAt&language=ru&apiKey={api}').json()
    with open('news', "wb") as file:
        pickle.dump(news, file)

