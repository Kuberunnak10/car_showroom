from django.core.mail import send_mail


def mail_sender(mark_name, mark_id):
    subject = 'Created new mark'
    message = f'Created new mark - {mark_name}, ID = {mark_id}'
    from_email = 'your-email@example.com'
    recipient_list = ['recipient@example.com']
    send_mail(subject, message, from_email, recipient_list)
