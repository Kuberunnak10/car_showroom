from django.apps import AppConfig


class AppAutosalonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_autosalon'

    def ready(self):
        import app_autosalon.signals
