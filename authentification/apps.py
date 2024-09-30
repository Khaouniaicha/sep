from django.apps import AppConfig


class TokenAuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentification'

    def ready(self):
        import authentification.signals