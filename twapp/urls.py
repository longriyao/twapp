"""twapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from firstapp.views import CashOrders
from firstapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='Orders'),
    url(r'^froms/',views.add, name='Orders'),
    url(r'^success',views.add),
    url(r't538994135893/', include('t538994135893.urls')),
    url(r't542846726794/', include('t542846726794.urls')),
    url(r't543410226625/', include('t543410226625.urls')),
    url(r't544719568562/', include('t544719568562.urls')),
    url(r'projectapp/', include('projectapp.urls')),
]
