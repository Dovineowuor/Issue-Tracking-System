from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.Projects.models import Issue
from .models import Board, List, Card
from .serializers import BoardSerializer, ListSerializer, CardSerializer, IssueSerializer

@api_view(['GET'])
def board_list(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    serializer = BoardSerializer(board)
    return Response(serializer.data)

@api_view(['POST'])
def create_board(request):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_board(request, board_id):
    board = Board.objects.get(id=board_id)
    serializer = BoardSerializer(board, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_board(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    return Response(status=204)

@api_view(['POST'])
def create_list(request, board_id):
    serializer = ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(board_id=board_id)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_card(request, list_id):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(list_id=list_id)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def assign_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.assigned_to = request.data.get('assigned_to')
    issue.save()
    serializer = IssueSerializer(issue)
    return Response(serializer.data)

@api_view(['POST'])
def resolve_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.status = 'Resolved'
    issue.save()
    serializer = IssueSerializer(issue)
    return Response(serializer.data)

@api_view(['POST'])
def reassign_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.assigned_to = None
    issue.save()
    serializer = IssueSerializer(issue)
    return Response(serializer.data)

@api_view(['POST'])
def manage_roles(request, role_id):
    # Your code here
    return Response(status=200)
