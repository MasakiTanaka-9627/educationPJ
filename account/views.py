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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
import io
import matplotlib.pyplot as plt

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

#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s


# html表示view
def analysis_screen(request):
    return render(request, 'analysis.html')

#画像埋め込み用view
def img_plot(request):
    # matplotを使って作図する
    x = [1, 5, 9]
    y = [4, 6, 8]
    ax = plt.subplot()
    ax.scatter(x, y)
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response

def graph2():
    import matplotlib.pyplot
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    import random
    import string
    import os

    class TempImage(object):

        def __init__(self, file_name):
            self.file_name = file_name

        def create_png(self):
            fig, ax = matplotlib.pyplot.subplots()
            ax.set_title(u'IMINASHI GRAPH 2')
            x_ax = range(1, 284)
            y_ax = [x * random.randint(436, 875) for x in x_ax]
            ax.plot(x_ax, y_ax)

            canvas = FigureCanvasAgg(fig)
            canvas.print_figure(self.file_name)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            os.remove(self.file_name)

    chars = string.digits + string.letters
    img_name = ''.join(random.choice(chars) for i in xrange(64)) + '.png'

    with TempImage(img_name) as img:
        img.create_png()
        return send_file(img_name, mimetype='image/png')