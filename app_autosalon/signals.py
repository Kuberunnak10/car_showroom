from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from app_autosalon.models import Mark
from app_autosalon.utils import mail_sender


@receiver(post_save, sender=Mark)
def mark_signal(sender, instance, created, **kwargs):
    # if created:
    mark = Mark.objects.all()
    cache.set('cache_marks', mark)
    mail_sender(instance.name, instance.id)
