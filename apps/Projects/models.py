from django.db import models
from django.contrib.auth.models import User
from django_redis import get_redis_connection
from django.utils import timezone

redis_cache = get_redis_connection("default")


class Project(models.Model):
    STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('in_progress', 'In Progress'),
        ('not_started', 'Not Started'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')

    def __str__(self):
        return self.name

    @staticmethod
    def get_cached_projects():
        projects = redis_cache.get("projects")
        if projects is None:
            projects = list(Project.objects.all())
            redis_cache.set("projects", projects)
        return projects

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Issue(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('closed', 'Closed')]
    PRIORITY_CHOICES = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='open'
    )
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default='low'
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assigned_issues'
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_issues'
    )

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
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name='files', default=None
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='authored_comments',
    )
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name='comments'
    )

    def __str__(self):
        return self.text[:50] if len(self.text) > 50 else self.text

    @staticmethod
    def get_cached_comments(issue_id):
        comments = redis_cache.get("comments_{}".format(issue_id))
        if comments is None:
            comments = list(Comment.objects.filter(issue_id=issue_id))
            redis_cache.set("comments_{}".format(issue_id), comments)
        return comments
