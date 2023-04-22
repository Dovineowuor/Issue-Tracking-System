from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Avg
from .models import Project, Issue, Comment, File
from .models import Issue, Comment, File
# Analytics
# from .models import Analytics

@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        owner = request.user
        project = Project.objects.create(name=name, description=description, owner=owner)
        messages.success(request, 'Project created successfully.')
        return redirect('project_detail', project.id)
    return render(request, 'projects/create_project.html')

@login_required
def update_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        project.name = request.POST['name']
        project.description = request.POST['description']
        project.save()
        messages.success(request, 'Project updated successfully.')
        return redirect('project_detail', project.id)
    return render(request, 'projects/update_project.html', {'project': project})

@login_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    messages.success(request, 'Project deleted successfully.')
    return redirect('project_list')

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    issues = Issue.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {'project': project, 'issues': issues})

@login_required
def create_issue(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        assigned_to = request.POST['assigned_to']
        issue = Issue.objects.create(title=title, description=description, priority=priority, project=project, assigned_to=assigned_to, created_by=request.user)
        messages.success(request, 'Issue created successfully.')
        return redirect('issue_detail', issue.id)
    return render(request, 'projects/create_issue.html', {'project': project})

@login_required
def update_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        issue.title = request.POST['title']
        issue.description = request.POST['description']
        issue.priority = request.POST['priority']
        issue.assigned_to = request

@login_required
def analytics_view(request):
    analytics = Analytics()
    total_issues = analytics.get_total_issues()
    open_issues = analytics.get_open_issues()
    closed_issues = analytics.get_closed_issues()
    avg_priority = analytics.get_avg_priority()
    issues_per_project = analytics.get_issues_per_project()
    issues_per_user = analytics.get_issues_per_user()
    total_comments = analytics.get_total_comments()
    comments_per_issue = analytics.get_comments_per_issue()
    total_file_size = analytics.get_total_file_size()
    files_per_issue = analytics.get_files_per_issue()
    context = {
        'total_issues': total_issues,
        'open_issues': open_issues,
        'closed_issues': closed_issues,
        'avg_priority': avg_priority,
        'issues_per_project': issues_per_project,
        'issues_per_user': issues_per_user,
        'total_comments': total_comments,
        'comments_per_issue': comments_per_issue,
        'total_file_size': total_file_size,
        'files_per_issue': files_per_issue,
    }

    
    return render(request, 'analytics.html', context)
