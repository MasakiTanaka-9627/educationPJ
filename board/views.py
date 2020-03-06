from django.shortcuts import render
from .models import BoardModel
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class BoardCreate(CreateView):
    template_name = 'boardcreate.html'
    model = BoardModel
    fields = ('title', 'content', 'author')    
    success_url = reverse_lazy('boardcreate')
    def form_valid(self, form):
        self.object = post = form.save()
        messages.success(self.request, f'記事を作成しました。 タイトル:{post.title} pk:{post.pk}')
        return redirect(self.get_success_url())

def boardlistfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'boardlist.html', {'object_list':object_list})