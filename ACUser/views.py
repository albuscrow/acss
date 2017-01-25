from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.urlresolvers import reverse
from django.views import generic
from .models import User
from django.utils import timezone
from datetime import timedelta, datetime
import ACUser.ss.ss_manager as SSM
import re
import os


# Create your views here.
def index(request) -> HttpResponse:
    return render(request, 'ACUser/index.html')


def login(user_name: str, password: str) -> (str, User):
    error_message = "password or user name incorrect"
    try:
        u = User.objects.get(user_name__exact=user_name)  # type: User
        if u.password == password:
            return None, u
        else:
            return error_message, None
    except User.DoesNotExist:
        return error_message, None


def register(user_name: str, password: str) -> (str, User):
    if user_name is None or len(user_name) == 0:
        return 'user name con not be empty', None

    if not re.match('^[a-zA-Z0-9_.-]+$', user_name):
        return r'user name should be match ^[a-zA-Z0-9_.-]+$', None

    if User.objects.filter(user_name=user_name).exists():
        return 'user name is used by other ones', None
    else:
        u = User()
        u.user_name = user_name
        u.password = password
        u.expired_date = timezone.now()
        u.save()
        return None, u


def do_login_or_register(request: HttpRequest) -> HttpResponse:
    user_name = request.POST['username']
    password = request.POST['password']
    action = request.POST['action']
    if action == 'login':
        error_message, u = login(user_name, password)
    else:
        error_message, u = register(user_name, password)

    if error_message is not None:
        return render(request, 'ACUser/index.html', {"error_message": error_message})
    else:
        request.session['userid'] = u.id
        return HttpResponseRedirect(reverse('ACUser:user'))


def user_detail(request) -> HttpResponse:
    return render(request, 'ACUser/user.html', {
        'user': User.objects.get(pk=request.session['userid'])})


def renew(request, minutes):
    user = User.objects.get(pk=request.session['userid'])
    user.renew(timedelta(minutes=int(minutes)))
    SSM.update_ss_server()
    return redirect(reverse('ACUser:user'))


def stop_all(request):
    SSM.stop_all_ss_server()
    return redirect(reverse('ACUser:user'))
