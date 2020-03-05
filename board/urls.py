from django.urls import path
from .views import BoardCreate, boardlistfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', BoardCreate.as_view(), name='boardcreate'),
    path('list/', boardlistfunc, name='boardlist'),    
]