from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
class YourAppConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.signals