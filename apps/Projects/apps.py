# Older version of apps.py
# from django.apps import AppConfig

# class ProjectsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'apps.Projects'

# from django.apps import AppConfig

# class ProjectsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'apps.Projects'

#     def ready(self):
#         import apps.Projects.signals

from django.apps import AppConfig

class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Projects'

    def ready(self):
        from apps.Projects import signals