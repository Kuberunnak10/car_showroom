import time

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail

from app_autosalon.models import Mark


@shared_task
def mailsender():
    time.sleep(10)
    subject = 'hello'
    msg = 'world'
    send_mail(subject, msg, 'kuberunnak@ya.ru', ['qwerty@ya.ru',])


@shared_task
def mail_sender(mark_name, mark_id):
    subject = 'Created new mark'
    message = f'Created new mark - {mark_name}, ID = {mark_id}'
    from_email = 'your-email@example.com'
    recipient_list = ['recipient@example.com']
    send_mail(subject, message, from_email, recipient_list)


@shared_task
def update_cache_marks():
    mark = Mark.objects.all()
    cache.set('cache_marks', mark)
