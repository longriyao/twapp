#coding:utf-8
from django.db import models
from datetime import datetime

class CashOrders(models.Model):
    babyusername = models.CharField(verbose_name='产品中文名', max_length=20, default='')
    babyname = models.CharField(verbose_name='产品类别', max_length=20)
    clientname = models.CharField(verbose_name='收件人',max_length=20)
    mobile = models.CharField(verbose_name='手机号',max_length=15)
    price = models.FloatField(verbose_name='金额',max_length=10)
    email = models.EmailField(verbose_name='邮箱', default='')
    address = models.CharField(verbose_name='地址', max_length=30,default='')
    number = models.IntegerField(verbose_name='数量')
    remark = models.CharField(verbose_name='备注', max_length=50, default='')
    ordersnum =  models.CharField(verbose_name='订单序列号', max_length=60, default='')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '订单编号'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.add_time                #显示记录时，用name来区别

# Create your models here.
