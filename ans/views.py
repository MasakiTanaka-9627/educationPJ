from django.shortcuts import render
from .models import AnsModel
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST
from board.models import BoardModel

# Ans

def ans_createfunc(request):
    # if request.method == 'GET':
    #     return render(request, 'board_detail.html')

    if request.method == 'POST':
        post_content = request.POST.get('content')
        post_title = request.POST.get('title')
        post_author = request.POST.get('author')
        board_id = request.POST.get('board')
        ans_board = BoardModel.objects.get(pk=board_id)
        ans = AnsModel(
            content=post_content, author=post_author, board=ans_board
            )
        ans.save()
        messages.success(request, '回答を投稿しました。')
        return redirect('board_list')