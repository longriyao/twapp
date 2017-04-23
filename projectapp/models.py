from django.db import models
from datetime import datetime

class project(models.Model):
    projectId = models.IntegerField('taobaoid')
    projectName = models.CharField('babyname产品名称', max_length=60, default='')
    projectIndexImage = models.CharField('上滚主图片地址',max_length=9999, default='')
    projectDescribe = models.CharField('projectsDescribeHTML', max_length=9999)
    projectPrice = models.FloatField('默认价格',default=998)
    sellername =models.CharField('sellname商家账户', max_length=30)

    class Meta:
        verbose_name= '产品详情',
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.projectId

class projectColor(models.Model):
    projectcolorId = models.CharField(max_length=20)
    projectcolorname = models.CharField('babyname', max_length=60)
    projectcolortaiwanname = models.CharField('babyname', max_length=60, null=True)

    class Meta:
        verbose_name= '产品颜色',
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.projectcolorname

class projectColorImages(models.Model):
    projectId = models.ForeignKey(project)
    projectcolorId = models.ForeignKey(projectColor)
    projectColorImages = models.CharField('babyname', max_length=9999, null=True)

    class Meta:
        verbose_name= '顏色圖片',
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.projectcolorname

class projectSize(models.Model):
    projectSizeId = models.IntegerField('编号')
    projectSizename = models.CharField('尺码名', max_length=60)

    class Meta:
        verbose_name= '产品尺码表',
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.projectSizename

class projectSku(models.Model):
    projectSkuId = models.ForeignKey(project)
    projectColorId = models.ForeignKey(projectColor)
    projectSizeId = models.ForeignKey(projectSize)
    projectColorImages = models.ForeignKey(projectColorImages)
    projectSkuPrice = models.FloatField('产品价格')

    class Meta:
        verbose_name= 'sku价格',
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.projectSkoPrice

class SkuOrders(models.Model):
    projectSkuId = models.ForeignKey('projectSku')
    babyusername = models.CharField(verbose_name='产品中文名', max_length=20, default='')
    babyname = models.CharField(verbose_name='产品类别', max_length=20)
    clientname = models.CharField(verbose_name='收件人',max_length=20)
    mobile = models.CharField(verbose_name='手机号',max_length=15)
    price = models.FloatField(verbose_name='金额',max_length=10)
    email = models.EmailField(verbose_name='邮箱', default='')
    address = models.CharField(verbose_name='地址', max_length=30,default='')
    number = models.IntegerField(verbose_name='数量')
    remark = models.CharField(verbose_name='备注', max_length=50, default='')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '订单编号'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.SkoOrders                #显示记录时，用name来区别

class orderUser(models.Model):
    orderUser = models.ForeignKey('projectSku')
    babyusername = models.CharField(verbose_name='产品中文名', max_length=20, default='')
    babyname = models.CharField(verbose_name='产品类别', max_length=20)
    clientname = models.CharField(verbose_name='收件人', max_length=20)
    mobile = models.CharField(verbose_name='手机号', max_length=15)
    price = models.FloatField(verbose_name='金额', max_length=10)
    email = models.EmailField(verbose_name='邮箱', default='')
    address = models.CharField(verbose_name='地址', max_length=30, default='')
    number = models.IntegerField(verbose_name='数量')
    remark = models.CharField(verbose_name='备注', max_length=50, default='')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '订单用户'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.orderUser  # 显示记录时，用name来区别

                # Create your models here.

class orderaddress(models.Model):
    orderUser = models.ForeignKey(orderUser)
    address = models.CharField(verbose_name='地址', max_length=30, default='')

    class Meta:
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.address  # 显示记录时，用name来区别

                # Create your models here.