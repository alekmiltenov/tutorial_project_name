from django.apps import AppConfig


class TutorialRegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutorial_registration'

def ready(self):
    import tutorial_registration.signals