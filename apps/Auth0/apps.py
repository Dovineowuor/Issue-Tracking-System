from django.apps import AppConfig

class Auth0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Auth0'
    label = 'auth0'
    verbose_name = 'Auth0'
