from django.urls import path
from .views import BoardCreate, board_listfunc, board_detailfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', board_listfunc, name='board_list'),
    path('detail/<int:pk>', board_detailfunc, name='board_detail'),
    path('create/', BoardCreate.as_view(), name='board_create'),    
]