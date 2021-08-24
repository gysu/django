"""Html_Form01 URL Configuration

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
from mysite import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_example/', views.get_example),
    path('', views.index),
    path('<int:pid>/<str:del_pass>',views.index),#GET的刪除都放在index不是很好 要拆開
    path('list/',views.listing),#將顯示與貼文獨立出來 list負責顯示訊息
    path('post/',views.posting),#post 負責貼文
    path('contact/',views.contact),#聯絡我forms表單 讓表單自動生成
    path('post2db/',views.post2db),#張貼 貼文用modelform顯示欄位
    path('captcha/', include('captcha.urls')) #機器人驗證對應網址
    ]