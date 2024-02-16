import time

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def mailsender():
    time.sleep(10)
    subject = 'hello'
    msg = 'world'
    send_mail(subject, msg, 'kuberunnak@ya.ru', ['qwerty@ya.ru',])
