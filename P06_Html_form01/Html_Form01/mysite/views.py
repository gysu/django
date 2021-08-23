from django.shortcuts import render

# Create your views here.

from mysite import models
from mysite import forms

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives




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



#負責顯示
def listing(request):
  posts = models.Post.objects.filter(enabled = True).order_by('-pub_time')[:150]
  moods = models.Mood.objects.all()
  return render(request,"listing.html", locals())
#張貼文改用Post
def posting(request):
  posts = models.Post.objects.filter(enabled = True).order_by('-pub_time')[:150]
  moods = models.Mood.objects.all()
  try:
    user_id = request.POST['user_id']
    user_pass = request.POST['user_pass']
    user_post = request.POST['user_post']
    user_mood = request.POST['mood']
  except:
      user_id = None
      message="每個欄位都須填寫"
 #存入資料庫
  if user_id != None:
  #  print(user_id,user_pass,user_post,user_mood)
    urmood = models.Mood.objects.get(status = user_mood) #喜怒哀樂
    post = models.Post.objects.create(mood=urmood,nickname=user_id,del_pass=user_pass,message=user_post)
    post.save()
    message ="儲存成功,請記得你的編輯密碼[{}]!，訊息需經審查後才會顯示。".format(user_pass)

  return render(request,"post.html",locals())

#聯絡我 post接收 寄出mail
def contact(request):
  #post方法可以用forms可以直接接收post欄位,就不用每個欄位都寫post
  if request.method =='POST': #判斷是不是用POST傳入
    form = forms.ContactForm(request.POST) #自動帶入POST欄位
    if form.is_valid():#檢查表單正確性
      #查看資料是否有正確傳來
      user_name = form.cleaned_data['user_name']
      user_city = form.cleaned_data['user_city']
      user_school = form.cleaned_data['user_school']
      user_email = form.cleaned_data['user_email']
      user_message = form.cleaned_data['user_message']
      message = "感謝你的來信"

      #寄信
      mail_body = "網友姓名：{} 居住城市：{} 是否在學：{} 反應意見：如下 {}".format(user_name, user_city, user_school, user_message)
      msg = EmailMultiAlternatives(
          subject="來自【NTU亂亂賣】網站的網友意見",
          body=mail_body,
          from_email=user_email,
          to=["	benqv777@gmail.com"], #只能發給自己
          reply_to=["Helpdesk <support@example.com>"])
      # Send it:
      msg.send()
    else:
      message="請檢查您輸入的資訊是否正確"
  else:
    form = forms.ContactForm() #接收forms欄位直接渲染到畫面 就不用每個欄位都寫post

  return render(request,"contact.html",locals())