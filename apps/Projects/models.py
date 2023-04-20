from django.db import models
# from django.contrib.auth.models import User
# from apps.Projects.models.apps import Project
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_issues')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_issues')

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# # Analytics imports
# from django.db.models import Count, Sum, Avg
# from apps.Projects.models import Comment, File, Issue
# # issues  no module on line six refered so

# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

# class Issue(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])
#     priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_issues')
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_issues')
# # Commenting
# class Comment(models.Model):
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # File Handling
# class File(models.Model):
#     name = models.CharField(max_length=255)
#     file = models.FileField(upload_to='files/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

# class Issue(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])
#     priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_issues')
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_issues')

# class Comment(models.Model):
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class File(models.Model):
#     name = models.CharField(max_length=255)
#     file = models.FileField(upload_to='files/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # Analytics of the Issues and related metrics
# # Check on Automatic Memo Handling and notification, either through a document or just text or email
# # Immediate Issue Creation or seconds after issue creation


# class Analytics:
#     def __init__(self):
#         pass

#     def get_total_issues(self):
#         return Issue.objects.count()

#     def get_open_issues(self):
#         return Issue.objects.filter(status='open').count()

#     def get_closed_issues(self):
#         return Issue.objects.filter(status='closed').count()

#     def get_avg_priority(self):
#         return Issue.objects.aggregate(Avg('priority'))

#     def get_issues_per_project(self):
#         return Issue.objects.values('project__name').annotate(num_issues=Count('id'))

#     def get_issues_per_user(self):
#         return Issue.objects.values('assigned_to__username').annotate(num_issues=Count('id'))

#     def get_total_comments(self):
#         return Comment.objects.count()

#     def get_comments_per_issue(self):
#         return Comment.objects.values('issue__title').annotate(num_comments=Count('id'))

#     def get_total_file_size(self):
#         return File.objects.aggregate(Sum('file__size'))

#     def get_files_per_issue(self):
#         return File.objects.values('issue__title').annotate(num_files=Count('id'))

# Updated Version2

# from django.db import models
# from django.contrib.auth.models import User
# from apps.Projects.models import Project
# class Issue(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])
#     priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_issues')
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_issues')

# class Comment(models.Model):
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class File(models.Model):
#     name = models.CharField(max_length=255)
#     file = models.FileField(upload_to='files/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# Updated Version 3

