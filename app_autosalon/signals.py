from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from app_autosalon.models import Mark
from app_autosalon.tasks import update_cache_marks
from app_autosalon.tasks import mail_sender


@receiver(post_save, sender=Mark)
def mark_signal(sender, instance, created, **kwargs):
    # if created:
    update_cache_marks()
    mail_sender.delay(instance.name, instance.id)
