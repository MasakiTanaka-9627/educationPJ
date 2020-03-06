from django.shortcuts import render
from .models import BoardModel
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class BoardCreate(CreateView):
    template_name = 'board_create.html'
    model = BoardModel
    fields = ('title', 'content', 'author')    
    success_url = reverse_lazy('board_create')
    
    def form_valid(self, form):
        self.object = post = form.save()
        messages.success(self.request, f'記事を作成しました。 タイトル:{post.title} pk:{post.pk}')
        return redirect(self.get_success_url())

def board_listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'board_list.html', {'object_list':object_list})

def board_detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'board_detail.html', {'object':object})
