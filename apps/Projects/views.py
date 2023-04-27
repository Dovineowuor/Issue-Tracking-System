from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Issue, Comment, File
from apps.Board.models import Board, User, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, FileSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import FileSerializer
from .models import File

@api_view(['GET'])
def get_file(request, id):
    file = File.objects.get(id=id)
    serializer = FileSerializer(file)
    return JsonResponse(serializer.data)


@login_required
@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@login_required
@api_view(['PUT'])
def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@login_required
@api_view(['DELETE'])
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return Response(status=204)


@login_required
@api_view(['GET'])
def issue_list(request):
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    serializer = IssueSerializer(issue)
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def create_issue(request):
    serializer = IssueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@login_required
@api_view(['PUT'])
def update_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    serializer = IssueSerializer(instance=issue, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@login_required
@api_view(['DELETE'])
def delete_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    issue.delete()
    return Response(status=204)


@login_required
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@login_required
@api_view(['PUT'])
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return