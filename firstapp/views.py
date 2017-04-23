#coding:utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from .models import CashOrders
import time
from datetime import datetime

# Create your views here.
res = 998
res2 = 1298
babyname = '爆款女包'
def index(req):
    #return HttpResponse('t2+t3')
    if req.method == 'POST':
       t2=req.POST['num']#数量
       print(type(t2))
       t3=req.POST['color']#颜色
       print(type(res))
       t4=int(t2)*res #金额
       print(t4)
       response = HttpResponseRedirect('/froms')
       response.set_cookie('num',t2)
       response.set_cookie('color',t3)
       response.set_cookie('money',t4)

       return response
    else:
       return render(req, 'static/index1.html', {'res': res, 'babyname':babyname})

def add(req):
  if req.method == 'POST':
   num = req.COOKIES.get('num','')#获取购买的数量
   color=req.COOKIES.get('color','')#获取颜色
   money=req.COOKIES.get('money','')#获取总金额
   name = req.POST['name']#名字
   mob = req.POST['mob']#电话号
   mail = req.POST['email']#邮箱
   address = req.POST['address']#地址
   #postal = req.POST['postal']#右边
   guest = req.POST['guest']#留言
   babyid = '531622432754'
   ordernum = int(time.mktime(datetime.now().timetuple()))
   print(ordernum)
   resa = CashOrders.objects.create(babyname=color, clientname=name, mobile=mob, price=res, email=mail, address=address, number=num, remark=guest, babyusername=babyid, ordersnum=ordernum)

   resa.save()
   colorurl='/products/hermes326/'+color+'.jpg'
   return render(req, 'static/success.html', {'num':num,'color':color,'colorurl':colorurl,'money':money,'res':res})
  else:
   num = req.COOKIES.get('num','')#获取购买的数量
   color=req.COOKIES.get('color','')#获取颜色
   money=req.COOKIES.get('money','')#获取总金额
   colorurl='/products/hermes326/'+color+'.jpg'
   return render(req, 'static/payment.html', {'num':num,'color':color,'colorurl':colorurl, 'money':money})

def out(req):#用来清除cookie
   response = HttpResponse('out')
   response.delete_cookie('num')
   return response

