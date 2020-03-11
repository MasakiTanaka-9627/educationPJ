from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ans import views

urlpatterns = [
    path('create/', views.ans_createfunc, name='ans_create'),
    # path('detail/<int:pk>', views.ans_detailfunc, name='ans_detail'),
    # path('edit/<int:pk>', views.ans_editfunc, name='ans_edit'),    
    # path('delete/<int:pk>', views.ans_deletefunc, name='ans_delete'),
]