from celery import shared_task
from django.core.mail import send_mail

from app_profile.models import BookingModel


@shared_task
def send_booking_email(booking_id, auto_id, first_name, last_name, number_phone):
    booking = BookingModel.objects.get(pk=booking_id)
    subject = f'New booking - {auto_id} !'
    message = f'{first_name} {last_name}, Тел: {number_phone}, заинтересовался {auto_id}'
    from_email = 'your-email@example.com'
    recipient_list = ['recipient@example.com']
    send_mail(subject, message, from_email, recipient_list)
