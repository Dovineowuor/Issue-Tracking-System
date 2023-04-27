from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
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
        # Set the created_at and updated_at fields of the project and issue
        instance.created_at = timezone.now()
        instance.updated_at = timezone.now()
        instance.save()
        issue.created_at = timezone.now()
        issue.updated_at = timezone.now()
        issue.save()
