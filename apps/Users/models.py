from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from apps.Projects.models import Issue


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

from django.db import models
from django.contrib.auth.models import User
from apps.Projects.models import Issue, Project

class UserIssue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='assigned_issues_user')
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])

class Role(models.Model):
    name = models.CharField(max_length=20)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)