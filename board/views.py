from django.shortcuts import render
from .models import BoardModel
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST

# Board

class BoardCreate(CreateView):
    template_name = 'board_create.html'
    model = BoardModel
    fields = ('title', 'content', 'author')    
    success_url = reverse_lazy('board_list')
    
    def form_valid(self, form):
        self.object = post = form.save()
        messages.success(self.request, f'記事を作成しました。 タイトル:{post.title} pk:{post.pk}')
        return redirect(self.get_success_url())

def board_listfunc(request):
    boards = BoardModel.objects.all()
    return render(request, 'board_list.html', {'boards':boards})

def board_detailfunc(request, pk):
    board = BoardModel.objects.get(pk=pk)
    return render(request, 'board_detail.html', {'board':board})

@require_POST
def board_deletefunc(request, pk):
    board = get_object_or_404(BoardModel, id=pk)
    board.delete()
    return redirect('board_list')