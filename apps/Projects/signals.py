from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.Projects.models import Project

# @receiver(post_save, sender=Project)
# def project_created(sender, instance, created, **kwargs):
#     if created:
#         # Do something when a new project is created
#         pass

from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.Projects.models import Project, Issue

@receiver(post_save, sender=Project)
def project_created(sender, instance, created, **kwargs):
    if created:
        # Create a new issue for the project
        issue = Issue.objects.create(
            title=f"New project: {instance.name}",
            description=f"A new project '{instance.name}' has been created.",
            status='open',
            priority='medium',
            project=instance,
            assigned_to=instance.manager,
            created_by=instance.manager
        )