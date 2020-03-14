from django.shortcuts import render
from .models import BoardModel, BoardImage
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST
from account.models import User
from ans.models import AnsModel
from .forms import BoardImageForm

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
        board = BoardModel(
            title=post_title, content=post_content, author=user
        )
        board.save()
        form.image = request.FILES.get('image')
        form = BoardImageForm(request.POST, request.FILES)
        form.save()
        messages.success(request, '記事を作成しました。')
        return redirect('board_list')


def board_listfunc(request):
    boards = BoardModel.objects.all().order_by('-created_at')
    for board in boards:
        board.ans_count = AnsModel.objects.filter(board_id_id=board.id).count()
    return render(request, 'board_list.html', {'boards': boards})


def board_detailfunc(request, pk):
    board = BoardModel.objects.get(pk=pk)
    ans_all = AnsModel.objects.filter(board_id_id=pk)
    return render(request, 'board_detail.html', {'board': board, 'ans_all': ans_all})


@require_POST
def board_deletefunc(request, pk):
    board = get_object_or_404(BoardModel, id=pk)
    board.delete()
    return redirect('board_list')


def board_editfunc(request, pk):
    board = get_object_or_404(BoardModel, id=pk)

    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('board_detail', pk)

    return render(request, 'board_create.html', {'board': board})


def showall(request):
    images = BoardImage.objects.all()
    context = {'images': images}
    return render(request, 'showall.html', context)


def upload(request):
    if request.method == "POST":
        form = BoardImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showall')
    else:
        form = BoardImageForm()

    context = {'form': form}
    return render(request, 'upload.html', context)
