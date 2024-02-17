import requests
import datetime

now = datetime.date.today()
yesterday = now - datetime.timedelta(days=1)

link = requests.get(f'https://newsapi.org/v2/everything?q=auto&from={yesterday}&sortBy=publishedAt&language=ru&apiKey=220b041da53b40af8475733c796b137a').json()
# print(link)
a = link['articles']
for i in a:
    print(i)
