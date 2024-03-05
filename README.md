docker run -p 6379:6379 --name my-redis -d redis
celery -A core worker --pool=solo -l info
celery -A core beat -l info
python manage.py runserver
