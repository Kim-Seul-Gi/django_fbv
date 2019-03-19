from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm

# Create your views here.

def index(request):
    boards = Board.objects.order_by('-pk')
    context = {
        'boards' : boards
    }
    return render(request, 'boards/index.html', context)

def new(request):
    
    if request.method == 'POST':
        
        board_form = BoardForm(request.POST)
        
        if board_form.is_valid():
            
            # title = board_form.cleaned_data.get('title')
            # content = board_form.cleaned_data.get('content')
            # board = Board(title=title, content=content)
            # board.save()
            board=board_form.save() # 위 4줄과 같음
            
            return redirect(board)
    else:
        board_form = BoardForm()
        
    context = {'board_form':board_form} 
        
    return render(request, 'boards/form.html', context)
    
def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board=get_object_or_404(Board, pk=board_pk) # 없는 pk에 대한 요청을 반환하기 위함.
    board.hit += 1
    board.save()
    context = {'board':board}
    return render(request, 'boards/detail.html', context)
    
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect(board)
        
def edit(request, board_pk):
    # 1. board_pk 에 해당하는 오브젝트를 가져온다. 
    #    - 없으면, 404 에러
    #    - 있으면, board=Board.objects.get(pk=board_pk)
    board=get_object_or_404(Board, pk=board_pk)
    
    # 2-1. POST 요청이면 (사용자가 form을 통해 데이터를 보내준 것) 
    if request.method =='POST':
        # 사용자 입력값(request.POST)을 BoardForm에 전달해주고
        board_form = BoardForm(request.POST, instance=board) # 수정할때에는 instance필요
        # 검증을 판단한다.
        if board_form.is_valid():
            
            # title = board_form.cleaned_data.get('title')
            # content = board_form.cleaned_data.get('content')
            # board = Board(title=title, content=content)
            # board.save()
            board=board_form.save()
            
            return redirect(board)    
    # 2-2. GET 요청이면 (수정하기 버튼을 눌렀을 때)
    else: 
        # BoardForm을 초기화 (사용자 입력값을 넣어준 상태)
        board_form = BoardForm(instance=board)
    # context에 담겨있는 board_form은
    # (1) - POST 요청 결과 검증 실패한 상태
    # (2) - GET 요청에서 초기화된 상태
    context = {'board_form':board_form}
    
    return render(request, 'boards/form.html', context)
    
    
