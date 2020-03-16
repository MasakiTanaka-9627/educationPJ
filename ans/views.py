from django.shortcuts import render
from .models import AnsModel, AnsImage
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
        post_author = request.POST.get('user')
        board_id = request.POST.get('board')
        ans_board = BoardModel.objects.get(id=board_id)
        ans = AnsModel(
            content=post_content, author=post_author, board_id=ans_board
        )
        ans.save()

        post_image = request.FILES['image']
        board_image = AnsImage.objects.create(
            image=post_image, ans_id=ans.id
        )
        board_image.save()

        messages.success(request, '回答を投稿しました。')
        return redirect('board_list')


def ans_detailfunc(request, pk):
    ans = AnsModel.objects.get(pk=pk)
    return render(request, 'ans_detail.html', {'ans': ans})
