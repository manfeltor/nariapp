from django.apps import AppConfig

class CultivationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cultivationapp'

    def ready(self):
        import cultivationapp.signals.plant
