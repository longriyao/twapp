from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import projectSku, project, projectColorImages
from firstapp.models import CashOrders
import time
from datetime import datetime
import re
import urllib
def index(req, babyid):
    #return HttpResponse('t2+t3')
    if req.method == 'POST':
        print(babyid)
        num = req.POST['num']  # 数量
        size = req.POST['size']  # 数量
        price = req.POST['price']  # 数量
        totalprice = req.POST['totalprice']  # 数量
        imagesurl = req.POST['imagesurl']
        projectname = req.POST['projectname']
        color = req.POST['color']  # 颜色
        response = HttpResponseRedirect('/projectapp/froms/')
        response.set_cookie('num', num)
        response.set_cookie('price', price)
        response.set_cookie('totalprice', totalprice)
        response.set_cookie('color', color)
        response.set_cookie('size', size)
        response.set_cookie('babyid', babyid)
        response.set_cookie('imagesurl', imagesurl)
        response.set_cookie('projectname', urllib.parse.quote(projectname))
        return response

    else:
        resa = projectSku.objects.filter(projectSkuId__projectId=babyid) #通过projectSkuId到projectId查询babyid
        projectvalue = project.objects.filter(projectId=babyid) #获取产品信息
        projectname = '' #产品名称
        skuJson = [] #存skuJson数据
        for i in projectvalue: #读取project的数据表单的值
            projectname = i.projectName
            projectimage = re.split(',',i.projectIndexImage) #图片详情页数据
            projectDescribe = i.projectDescribe #读取详情页数值
            projectPrice = i.projectPrice #产品默认价格
            print(projectimage) #打印主图
        color =[];
        for i in resa:
            item = {
                "name": i.projectColorId.projectcolorname,
                "taiwanname": i.projectColorId.projectcolortaiwanname,
                "image": i.projectColorImages.projectColorImages,
            };
            if item in color:

                continue
            color.append(item);
        size = [];
        for i in resa:
            item = {
                "name":i.projectSizeId.projectSizename,
                "price":i.projectSkuPrice
            };
            if item in size:

                continue
            size.append(item);
        print(len(size))
        sizelen = len(size)
        print(size)
        return render(req, 'static/index2.html',{'projectvalue':projectvalue, 'skuJson':skuJson,'projectimage':projectimage,'projectname':projectname,'projectDescribe':projectDescribe,'projectPrice':projectPrice,'resa':resa,'color':color,'size':size,'sizelen':sizelen})

def add(req):
    if req.method == 'POST':
        num = req.COOKIES.get('num', '')  # 获取购买的数量
        color = req.COOKIES.get('color', '')  # 获取颜色
        size = req.COOKIES.get('size', '')  # 獲取尺碼
        imagesurl = req.COOKIES.get('imagesurl', '')  # 獲取尺碼
        print(color)
        # money = req.COOKIES.get('money', '')  # 获取总金额
        name = req.POST['name']  # 名字
        mob = req.POST['mob']  # 电话号
        mail = req.POST['email']  # 邮箱
        address = req.POST['address']  # 地址
        price = req.COOKIES.get('price', '')  # 金额
        totalprice = req.COOKIES.get('totalprice', '')  # 获取购买的数量
        nowtime = datetime.now()
        ordernum = int(time.mktime(datetime.now().timetuple()))

        guest = req.POST['guest']  # 留言
        projectname = urllib.parse.unquote(req.COOKIES.get('projectname', ''))
        babyid = req.COOKIES.get('babyid', '')  #产品id
        resa = CashOrders.objects.create(babyname=color, clientname=name, mobile=mob, price=num, email=mail,address=address, number=num, remark=guest, babyusername=babyid,ordersnum=ordernum)
        resa.save()
        return render(req, 'static/projecthtml/success.html', {'mob':mob, 'mail':mail, 'ordernum':ordernum, 'nowtime':nowtime, 'projectname':projectname, 'totalprice':totalprice, 'price':price, 'address':address, 'name':name, 'size':size, 'num': num, 'color': color, 'babyname': babyid,'imagesurl':imagesurl})
    else:
        num = req.COOKIES.get('num', '')  # 获取购买的数量
        price = req.COOKIES.get('price', '')  # 金额
        totalprice = req.COOKIES.get('totalprice', '')  # 获取购买的数量
        color = req.COOKIES.get('color', '')  # 获取颜色
        babyid = req.COOKIES.get('babyid', '')  # babyid
        imagesurl = req.COOKIES.get('imagesurl', '')  # babyid
        projectname = urllib.parse.unquote(req.COOKIES.get('projectname', ''))

        return render(req, 'static/projecthtml/payment.html',
                          {'num': num, 'color': color, 'imagesurl': imagesurl, 'totalprice': totalprice,'price':price,'babyid':babyid,'projectname':projectname})

# Create your views here.
