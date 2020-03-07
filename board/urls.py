from django.urls import path
from .views import BoardCreate
from django.conf import settings
from django.conf.urls.static import static
from board import views

urlpatterns = [
    path('create/', BoardCreate.as_view(), name='board_create'),
    path('list/', views.board_listfunc, name='board_list'),
    path('detail/<int:pk>', views.board_detailfunc, name='board_detail'),
    path('delete/<int:pk>', views.board_deletefunc, name='board_delete'),
]