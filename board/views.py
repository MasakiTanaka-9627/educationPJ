from django.shortcuts import render
from .models import BoardModel
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST

# Board

def board_createfunc(request):
    if request.method == 'GET':
        return render(request, 'board_create.html')
            
    if request.method == 'POST' & (not request.POST.get('author')):
        post_content = request.POST['content']
        print(post_content)
        return render(request, 'board_create.html', {'content':post_content})
        
    if request.method == 'POST':
        post_title = request.POST['title']
        post_content = request.POST['content']
        post_author = request.POST['author']
        board = BoardModel(title=post_title, content=post_content, author=post_author)
        board.save()
        messages.success(request, '記事を作成しました。タイトル:{post.title}')
        return redirect('board_list')

def board_listfunc(request):
    boards = BoardModel.objects.all().order_by('-created_at')
    return render(request, 'board_list.html', {'boards':boards})

def board_detailfunc(request, pk):
    board = BoardModel.objects.get(pk=pk)
    return render(request, 'board_detail.html', {'board':board})

@require_POST
def board_deletefunc(request, pk):
    board = get_object_or_404(BoardModel, id=pk)
    board.delete()
    return redirect('board_list')