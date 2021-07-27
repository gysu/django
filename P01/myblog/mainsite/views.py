from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template
# Create your views here.
def homepage(request):
  template = get_template('index.html')
  posts =Post.objects.all()
  now = datetime.now()
  html = template.render(locals())  #回傳區域變數用字典型態打包 一定要字典
  return HttpResponse(html)
  
def showpost(request,slug):
  template =get_template('post.html')
  try:
   post =Post.objects.get(slug=slug)
   if post != None:
       html = template.render(locals())  #回傳區域變數用字典型態打包 一定要字典
       return HttpResponse(html)
  except:
    #如果slug不存在資料庫就回去首頁
    return redirect('/')
# --------------參考----
# def showtemplate(request):
#     vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
#     context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
#     return render(request, 'test.html', context)

# ---------------參考----
# from .models import Topic # 匯入Topic模型

# def index(request):
#     return render(request, 'learning_logs/index.html')

# # 顯示所有主題
# def topics(request):
#     topics = Topic.objects.order_by('date_added')
#     context = {'topics': topics}   
#     return render(request, 'learning_logs/topics.html', context)

# # 顯示個別主題和它的entries
# def topic(request, topic_id):
#     topic = Topic.objects.get(id=topic_id)
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'learning_logs/topic.html', context)