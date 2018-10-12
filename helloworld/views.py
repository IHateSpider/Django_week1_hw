from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage
import random

'''
def index(request):
	return render(request, 'guestbookver1.html')   
'''
'''
def add(request):
   # c = int(a) + int(b)
    #return HttpResponse(str(c))
    return HttpResponse("https://picsum.photos/200/200?image=87")
''' 
def index(request):
    '''
    l = []
    ran_list = []
    for i in range(0, 15):
        random.seed()
        ran_list.append( random.randint(1, 1089) )
    for i in ran_list:
        l.append("https://picsum.photos/200/200?image="+str(i))
    return render(request, 'guestbookver1.html', {"fuck": l})
    '''
    t1 = TextMessage.objects.create(talker='草地音樂祭', message='已送交公關部進行拉贊')
    t2 = TextMessage.objects.create(talker='桌遊大會', message='昨日已圓滿完成')
    t3 = TextMessage.objects.create(talker='院櫃租借事宜', message='文案撰寫中')
    
    msgs = TextMessage.objects.all()
    
    return render(request, 'guestbookver1.html', locals())

    