from django.apps import AppConfig


class AlphavantageapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AlphaVantageAPI'

    def ready(self):
        from . import tasks
        tasks.start()
