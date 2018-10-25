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
def here(request):
    return HttpResponse('嗨嗨嗨\\ ')
    
def math(request, a, b):
    a = int(a)
    b = int(b)
    m = a*b
    q = a//b
    add = a + b
    minus = a - b 
    html = '<html>sum={add}<br>dif={minus}<br>pro={m}<br>quo={q}</html>'.format(add=add,minus=minus,m=m,q=q)
    return HttpResponse(html)
    

    
def welcome(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render(request, 'welcome.html',locals())
        
def adduser(request):
    if 'add_user' in request.POST:
        name = request.POST['add_user']
        password = request.POST['add_password']
        try:
            user=User.objects.get(username=name)
        except:
            user=None
    
        if user != None:
            mes = user.username + '帳號已建立!'
            return HttpResponse(mes)
        else:
            user = User.objects.create_user( name, "jj@jj.com.tw", password )
            user.first_name="aa"
            user.last_name="aa"
            user.is_staff=False
            user.save()
            return redirect('/login/')
    return render(request, 'adduser.html',locals())
    
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
    '''
    t1 = TextMessage.objects.create(talker='ddd', message='ccc')
    t2 = TextMessage.objects.create(talker='桌遊大會', message='昨日已圓滿完成')
    t3 = TextMessage.objects.create(talker='院櫃租借事宜', message='文案撰寫中')
    '''
    path = request.path
    #auth.logout(request)
    if 'name' in request.POST:
        t = TextMessage.objects.create(talker = request.POST['name'], message = request.POST['msg'])
    if 'clear' in request.POST:
        TextMessage.objects.all().delete()
    msgs = TextMessage.objects.all()
    return render(request, 'guestbookver1.html', locals())
    
def login(request):
    if 'username' in request.POST:
        name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/index/')
                message = '登入成功'
            else:
                message = '帳號尚未啟用'
        else:
            message = '登入失敗!'
    return render(request, 'login.html', locals())
    
def logout(request):
    auth.logout(request)
    return redirect('/index/')
    

    