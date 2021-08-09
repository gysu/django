"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainsite.views import homepage,showpost
from mysite import views as MTV_views
from django.conf.urls import include

MTV_urlpatterns = [
    # path('admin/', admin.site.urls),
    path('MTVhome/',  MTV_views.MTVhome),
    path('about/',  MTV_views.about),
    path('listing/',  MTV_views.listing),
    path('list/',  MTV_views.listing2), #這是用view寫
    path('listing/<sku>/',  MTV_views.disp_detail),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    #     post頁面底下的/slugid 第一個slug型態:第二個是資料欄位名稱 也可以簡化<slug>就好
    path('post/<slug:slug>/',showpost),
    path('MTV/',include(MTV_urlpatterns)),  #加入子網域

]
