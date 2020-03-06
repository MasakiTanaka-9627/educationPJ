from django.urls import path
from .views import homefunc, signupfunc, logoutfunc, loginfunc, user_listfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homefunc, name='home'),    
    path('signup/', signupfunc, name='signup'),
    path('logout/', logoutfunc, name='logout'),
    path('login/', loginfunc, name='login'),
    path('userlist/', user_listfunc, name='user_list'),    
]