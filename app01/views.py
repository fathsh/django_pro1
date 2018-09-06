from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app01 import models
import json
import os


def index(request):
    return render(request,"index.html")


def index1(request):
    return render(request,"index1.html")

def form(request):
    return render(request,"form.html")

def tab(request):
    return render(request,"tab.html")

def test(request):
    return render(request,"test.html")

def userInfo(request):
    res={'status':0,  'message':''}
    page=json.loads(list(request.GET.keys())[0]).get('page',1)
    limit=json.loads(list(request.GET.keys())[0])['limit']
    user_list=list(models.UserInfo.objects.all().values())
    print(user_list)
    res['total'] = len(user_list)
    paginator = Paginator(user_list, limit)
    try:
        # print(page)
        user_list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        user_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    user_list=list(user_list)
    res['data']=user_list
    # res['total']=len(user_list)
    # res['total']=100
    return HttpResponse(json.dumps(res))
    # return render(request,"tt.html",locals())

def userInfo_add(request):
    for i in range(100):
        models.UserInfo.objects.create(username='hjfdg{}'.format(i),password='ddfd')
    return HttpResponse('dddsds')

def av(request):
    return render(request,"av.html")

def aa(request):
    dir = "E:\\Django\\pro7\\static\\img"
    files = os.listdir(dir)
    return render(request,"aa.html",locals())



