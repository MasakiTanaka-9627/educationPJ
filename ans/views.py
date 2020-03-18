from django.shortcuts import render
from .models import Ans
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST
from board.models import Board

# Ans

def ans_createfunc(request):
    # if request.method == 'GET':
    #     return render(request, 'board_detail.html')

    if request.method == 'POST':
        post_content = request.POST.get('content')
        post_title = request.POST.get('title')
        post_author = request.POST.get('user')
        board_id = request.POST.get('board')
        ans_board = Board.objects.get(id=board_id)

        try:
            post_image = request.FILES['image']
            ans = Ans(
                content=post_content, author=post_author, board_id=ans_board, image=post_image
            )
            ans.save()
            messages.success(request, '回答を投稿しました。')
            return redirect('board_list')
        except:
            ans = Ans(
                content=post_content, author=post_author, board_id=ans_board
            )
            ans.save()
            messages.success(request, '回答を投稿しました。｜画像なし')
            return redirect('board_list')

def ans_detailfunc(request, pk):
    ans = Ans.objects.get(pk=pk)
    return render(request, 'ans_detail.html', {'ans': ans})
