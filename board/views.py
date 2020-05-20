from django.shortcuts import render
from .models import Board
from account.models import User
from ans.models import Ans
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.generic import CreateView

# Board

def board_createfunc(request):
    if request.method == 'GET':
        return render(request, 'board_create.html')

    if request.method == 'POST':
        post_content = request.POST.get('content')
        post_title = request.POST.get('title')
        user_id = request.POST.get('user')
        user = User.objects.get(pk=user_id)
        if post_title is None:
            return render(request, 'board_create.html', {'content': post_content})
        board = Board(
            title=post_title, content=post_content, author=user
        )
        board.save()
        try:
            post_image = request.FILES['image']
            messages.success(request, '記事を作成しました。')
            return redirect('board_list')
        except:
            return redirect('board_list')

def board_listfunc(request):
    boards = Board.objects.all().order_by('-created_at')
    for board in boards:
        board.ans_count = Ans.objects.filter(board_id=board.id).count()
    return render(request, 'board_list.html', {'boards': boards})

def board_detailfunc(request, pk):
    board = Board.objects.get(pk=pk)
    ans_all = Ans.objects.filter(board_id=pk).order_by('-created_at')
    return render(request, 'board_detail.html', {'board': board, 'ans_all': ans_all})


@require_POST
def board_deletefunc(request, pk):
    board = get_object_or_404(Board, id=pk)
    board.delete()
    return redirect('board_list')

def board_editfunc(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        try:
            baord.image = request.FILES['image']
            board.save()
            return redirect('board_detail', pk)
        except:
            board.save()
            return redirect('board_detail', pk)
    return render(request, 'board_create.html', {'board': board})
