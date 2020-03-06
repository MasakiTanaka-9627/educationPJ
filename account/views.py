from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        post_username = request.POST['username']
        post_email = request.POST['email']        
        post_password = request.POST['password']
        try:
            User.objects.get(username=post_username)
            messages.error(request, 'このユーザーは登録されています')
            return render(request, 'signup.html')
        except:
            user = User.objects.create_user(post_username, post_email, post_password)
            login(request, user)
            messages.success(request, 'ユーザー登録に成功しました')
            return render(request, 'home.html')
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        post_username = request.POST['username']
        post_password = request.POST['password']
        user = authenticate(request, username=post_username, password=post_password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logoutfunc(request):
    logout(request)
    return redirect('signup')

def user_listfunc(request):
    object_list = User.objects.all()
    return render(request, 'user_list.html', {'object_list':object_list})

def homefunc(request):
    return render(request, 'home.html')