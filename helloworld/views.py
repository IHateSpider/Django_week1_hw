from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

'''
def index(request):
	return render(request, 'guestbookver1.html')   
def add(request):
   # c = int(a) + int(b)
    #return HttpResponse(str(c))
    return HttpResponse("https://picsum.photos/200/200?image=87")
''' 
def guestbookver1(request):
    fuck = "fuck"
    return render(request, 'guestbookver1.html', {'fuck': fuck})