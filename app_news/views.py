import pickle

from django.shortcuts import render


def get_news(request):
    with open('news', 'rb') as file:
        data_news = pickle.load(file)
    return render(request, 'app_news/news.html', {'data_news': data_news})
