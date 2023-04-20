from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Issue
from .forms import ProjectForm, IssueForm

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
def delete_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.delete()
    messages.success(request, 'Issue deleted successfully.')
    return redirect('project_detail', issue.project.id)

@login_required
def issue_detail(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    return render(request, 'projects/issue_detail.html', {'issue': issue})