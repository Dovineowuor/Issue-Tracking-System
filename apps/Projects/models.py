from django.db import models
from django.contrib.auth.models import User
from apps.Board.models import Board
from django_redis import get_redis_connection
from django.utils import timezone

redis_cache = get_redis_connection("default")

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_cached_projects():
        projects = redis_cache.get("projects")
        if projects is None:
            projects = list(Project.objects.all())
            redis_cache.set("projects", projects)
        return projects

class Issue(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('closed', 'Closed')]
    PRIORITY_CHOICES = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_issues')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_issues')

    def __str__(self):
        return self.title

@staticmethod
def get_cached_issues(project_id):
    issues = redis_cache.get("issues_{}".format(project_id))
    if issues is None:
        issues = list(Issue.objects.filter(project_id=project_id))
        redis_cache.set("issues_{}".format(project_id), issues)
    return issues


class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='files', default=None)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_comments', default=models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_comments'))
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text[:50] + "..." if len(self.text) > 50 else self.text

    @staticmethod
    def get_cached_comments(issue_id):
        comments = redis_cache.get("comments_{}".format(issue_id))
        if comments is None:
            comments = list(Comment.objects.filter(issue_id=issue_id))
            redis_cache.set("comments_{}".format(issue_id), comments)
        return comments

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'apps':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'apps':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'apps' and obj2._meta.app_label == 'apps':
            return True
        return None
