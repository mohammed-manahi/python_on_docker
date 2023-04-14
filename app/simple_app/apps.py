from django.apps import AppConfig


class SimpleAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Update app name according to code organization
    name = 'app.simple_app'
