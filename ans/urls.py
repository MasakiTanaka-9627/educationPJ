from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from board import views

urlpatterns = [
    path('create/', views.board_createfunc, name='board_create'),
    path('list/', views.board_listfunc, name='board_list'),
    path('detail/<int:pk>', views.board_detailfunc, name='board_detail'),
    path('edit/<int:pk>', views.board_editfunc, name='board_edit'),    
    path('delete/<int:pk>', views.board_deletefunc, name='board_delete'),
]