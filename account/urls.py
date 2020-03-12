from django.urls import path
from .views import homefunc, signupfunc, logoutfunc, loginfunc, user_listfunc, user_detailfunc, user_editfunc
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account'

urlpatterns = [
    path('', homefunc, name='home'),    
    path('signup/', signupfunc, name='signup'),
    path('logout/', logoutfunc, name='logout'),
    path('login/', loginfunc, name='login'),
    path('userlist/', user_listfunc, name='user_list'),
    path('detail/<int:pk>', user_detailfunc, name='user_detail'),
    path('edit/<int:pk>', user_editfunc, name='user_edit'),
    path('analysis', views.analysis_screen, name='analysis_screen'),
    path('analysis/plot', views.img_plot, name="img_plot"),
]