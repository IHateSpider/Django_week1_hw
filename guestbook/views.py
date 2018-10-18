from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage

# Create your views here.
def talker_list(request):
    msgs = TextMessage.objects.all()
    return render(request, 'talker_list.html', locals())