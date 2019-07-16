import random
import time

from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.
from myblog.models import UserModel

global date_base
date_base = {}


def index(requset):
    token = requset.session.get('token')
    date = {'token': token}
    return render(requset, 'myblog/index.html', date)


def life(requset):
    return render(requset, 'myblog/life.html')


def skill(requset):
    return render(requset, 'myblog/skill.html')


def resources(request):
    return render(request, 'myblog/resources.html')


def about(request):
    return render(request, 'myblog/about.html')


def main(request):
    ticket = request.session.get('ticket')
    if ticket:
        try:
            user = UserModel.objects.get(ticket=ticket)
            print(111)
            print(user.ticket)
            date = {'user': user}
            print(2222)
            return render(request, 'myblog/main.html', date)
        except Exception as e:
            return redirect("/login")
    else:
        return redirect("/login")



def login(request):
    ticket = request.session.get('ticket')
    if ticket:
        return redirect('/main')
    else:
        return render(request, 'myblog/login.html')


def do_login(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        try:
            user = UserModel.objects.get(email = email)
            password = request.POST.get('user_password')
            if password == user.password:
                ticket = time.time() + random.randrange(1, 100000)
                user.ticket = ticket
                user.save()
                request.session['token'] = user.username
                request.session['ticket'] = ticket
                return redirect('/main')
            else:
                return redirect('/login')
        except Exception as e:
            return redirect('/login')
    else:
        return redirect('/login')


def register(request):
    return render(request, 'myblog/register.html')


def do_register(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        username = email
        try:
            user = UserModel.createUser(password, email, username)
            user.save()
            return redirect('/login')
        except Exception as e:
            return redirect('/register')
    else:
        return redirect('/register')


def quit(request):
    logout(request)
    return redirect('/index')
