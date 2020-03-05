from django.shortcuts import render
from .models import BoardModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class BoardCreate(CreateView):
    template_name = 'boardcreate.html'
    model = BoardModel
    fields = ('title', 'content', 'author')
    success_url = reverse_lazy('boardcreate')

def boardlistfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'boardlist.html', {'object_list':object_list})