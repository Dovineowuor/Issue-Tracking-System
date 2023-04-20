from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count, Sum, Avg
from .models import Project, Issue, Comment, File
from .models import Issue, Comment, File

# Analytics
# from .models import Analytics

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, 'Project created successfully.')
            return redirect('project_detail', project.id)
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

@login_required
def update_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Project updated successfully.')
            return redirect('project_detail', project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/update_project.html', {'form': form, 'project': project})

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
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.project = project
            issue.created_by = request.user
            issue.save()
            messages.success(request, 'Issue created successfully.')
            return redirect('issue_detail', issue.id)
    else:
        form = IssueForm()
    return render(request, 'projects/create_issue.html', {'form': form, 'project': project})

@login_required
def update_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save()
            messages.success(request, 'Issue updated successfully.')
            return redirect('issue_detail', issue.id)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'projects/update_issue.html', {'form': form, 'issue': issue})

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
