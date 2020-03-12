from django.shortcuts import render
from .models import User, Profile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from board.models import BoardModel
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required

# Account

def signupfunc(request):
    if not request.POST.get('username'):
        post_email = request.POST.get('email')
        return render(request, 'signup.html', {'email':post_email})
    if request.method == 'POST':
        post_username = request.POST['username']
        post_email = request.POST['email']
        post_password = request.POST['password']
        try:
            User.objects.get(username=post_username)
            messages.error(request, 'このユーザーは登録されています')
            return render(request, 'signup.html', {'email':post_email})
        except:
            user = User.objects.create_user(
                post_username, post_email, post_password)
            login(request, user)
            messages.success(request, 'ユーザー登録に成功しました')
            return render(request, 'home.html')
    return render(request, 'signup.html')


def loginfunc(request):
    if request.method == 'POST':
        post_username = request.POST['username']
        post_password = request.POST['password']
        user = authenticate(request, username=post_username,
                            password=post_password)
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
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_detailfunc(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'user': user})


def user_editfunc(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user_id=pk)
    if user.pk != request.user.pk:
        return redirect('home')
    if request.method  == "POST":
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        
        profile.location = request.POST.get("location")        
        profile.birth_day = request.POST.get("birth_day")        
        profile.introduction = request.POST.get("introduction")
        profile.save()
        user.save()
        return redirect('user_detail', pk)
    return render(request, 'user_edit.html', {'user': user})

def homefunc(request):
    boards = BoardModel.objects.filter(created_at__date=date.today()).order_by('-created_at')
    return render(request, 'home.html', {'boards': boards} )

