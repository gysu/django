"""myUrl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

my_patterns =[
    path('company/',views.company),
    path('sales/',views.sales),
    path('contact/',views.contact),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/<int:author_no>', views.about),
    path('about/', views.about), #about後面沒有參數時,導到預設參數
    path('info/',include(my_patterns)),  #加入子網域
    path('list/<int:yr>/<int:mon>/<int:day>',views.listing),
    path('post/<int:yr>/<int:mon>/<int:day>/<int:post_num>',views.post,name='post-url')
]
