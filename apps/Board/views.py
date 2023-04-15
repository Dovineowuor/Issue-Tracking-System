from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .models import Board, List, Card

def create_board(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        background = request.FILES.get('background')
        board = Board.objects.create(name=name, background=background)
        return redirect('board_detail', board_id=board.id)
    return render(request, 'create_board.html')

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    lists = List.objects.filter(board=board)
    cards = Card.objects.filter(list__in=lists)
    return render(request, 'board_detail.html', {'board': board, 'lists': lists, 'cards': cards})

def create_list(request, board_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        board = Board.objects.get(id=board_id)
        List.objects.create(name=name, board=board)
        return redirect('board_detail', board_id=board_id)

def create_card(request, list_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        background = request.FILES.get('background')
        pellets = request.FILES.get('pellets')
        list_obj = List.objects.get(id=list_id)
        Card.objects.create(name=name, description=description, due_date=due_date, background=background, pellets=pellets, list=list_obj)
        return redirect('board_detail', board_id=list_obj.board.id)

    
