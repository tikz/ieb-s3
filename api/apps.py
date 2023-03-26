import os

from django.apps import AppConfig


class APIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from api.threads import PriceUpdaterThread

        if os.environ.get('RUN_MAIN'):
            PriceUpdaterThread().start()
