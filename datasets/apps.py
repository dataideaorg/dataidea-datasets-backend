from django.apps import AppConfig


class DatasetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'datasets'

    def ready(self):
        """Import signals when Django starts"""
        import datasets.signals  # noqa
