from django.apps import AppConfig


class PrimaApplicazioneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prima_applicazione'

class SecondaApplicazioneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seconda_applicazione'
