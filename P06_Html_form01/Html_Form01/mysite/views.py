from django.shortcuts import render

# Create your views here.

from mysite import models

def get_example(request): 
  try:
    urid = request.GET['user_id']#接收表單NAME變數user_id
    urpass = request.GET['user_pass']#接收表單NAME變數user_pass
    ur_byear = request.GET['byear']#接收表單NAME變數byear
    urfcolor = request.GET.getlist('fcolor')#接收表單NAME變數fcolor checkbox
    urmovie = request.GET['fmovie']#接收表單NAME變數fcolor checkbox

  except:
    urid = None
  
  if urid != None and urpass == '123':
     verified = True
  else:
     verified = False
  years = range(1960,2022)
  return render(request, 'get_example.html',locals())

def index(request,pid=None,del_pass=None):
  posts=models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
  moods = models.Mood.objects.all()
  try:
    user_id = request.GET['user_id']
    user_pass = request.GET['user_pass']
    user_post = request.GET['user_post']
    user_mood = request.GET['mood']
  except:
      user_id = None
      message="每個欄位都須填寫"
  #get存入資料庫
  if user_id != None:
  #  print(user_id,user_pass,user_post,user_mood)
    urmood = models.Mood.objects.get(status = user_mood) #喜怒哀樂
    print(urmood,'666')
    post = models.Post.objects.create(mood=urmood,nickname=user_id,del_pass=user_pass,message=user_post)
    post.save()
    message ="儲存成功,請記得你的編輯密碼[{}]!，訊息需經審查後才會顯示。".format(user_pass)
 
  #get刪除資料庫
  if del_pass and pid:
    try:
      post = models.Post.objects.get(id=pid)      
    except:
      post = None

    if post:
      if post.del_pass == del_pass:
        post.delete()
        message = "資料刪除成功"
      else:
        message = "密碼錯誤"
  return render(request,"index.html",locals())