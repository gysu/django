from mysite.forms import PostForm
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
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
    #檢查’username’有沒有存在於Session中
  #如果有就把username以及useremail都取出來，再送去index.html中渲染網頁
  if 'username' in request.session:       
    username = request.session['username']
    usermail = request.session['useremail']
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
  if 'username' in request.session:       
    username = request.session['username']
    usermail = request.session['useremail']

  return render(request,"post.html",locals())

#聯絡我  Form應用 post接收 寄出mail  
def contact(request):
  #post方法可以用forms可以直接接收post欄位,就不用每個欄位都寫post
  if request.method =='POST': #判斷是不是用POST傳入
    form = forms.ContactForm(request.POST) #從forms.py抓資料準備渲染到DOM裡
    if form.is_valid():                    #檢查表單正確性     
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

import urllib
import json
from django.conf import settings
def post2db(request): #從資料庫產生的form 再從
  if request.method == "POST":
    post_form = forms.PostForm(request.POST)
    if post_form.is_valid():   #檢查DOM裡的資料是否正確
      recaptcha_response = request.POST.get('g-recaptcha-response')#google驗證 
      url = 'https://www.google.com/recaptcha/api/siteverify'      #google驗證 
      values = {                                                   #google驗證 
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
      }
      data = urllib.parse.urlencode(values).encode()               #google驗證 
      req = urllib.request.Request(url, data=data)                 #google驗證 
      response = urllib.request.urlopen(req)                       #google驗證 
      result = json.loads(response.read().decode())                #google驗證 
      ur_pass = post_form.cleaned_data.get('del_pass') #取得樣板所填寫的資料
      
      if result['success']:#google驗證
        if len(ur_pass)==0:
         message="您的訊息已儲存，要等管理者啟用後才看得到喔。"
         print(message)
         post_form.save()
        else:
          message="您的訊息已發布。"
          print(message)
          new = post_form.save(commit=False)  #先把這筆記錄commit起來
          new.enabled = True                  #可以改其他欄位
          new.save()                          #再儲存
          # post_form.save()            #儲存後畫面不會跳轉
        return redirect('/list/')#所以重導畫面
      else:
        message = "reCAPTCHA驗證失敗，請在確認."
    else:
      message = '每個欄位都須填寫'
  else:
    post_form = forms.PostForm() #從form.py
    moods = models.Mood.objects.all()
    message = '每個欄位都須填寫'
  return render(request,'post2db.html',locals())


#登入  session 的用法
def login(request):
  if request.method == 'POST':
     login_form = forms.LoginForm(request.POST) #
     if login_form.is_valid():                       
       login_name = request.POST['username'].strip() #抓forms.py的欄位值
       login_password = request.POST['password'] #抓forms.py的欄位值passwd值
       try:
          user = models.User.objects.get(name=login_name)  #檢查資料庫是否有使用者資訊
          if user.password == login_password:          #帳密一樣將資料記錄到Session中
            request.session['username'] = user.name    #設定session
            request.session['useremail'] = user.email  
            return redirect('/')
          else:
            message = "密碼錯誤"
       except:
          message = "找不到使用者"
  else:
    login_form = forms.LoginForm()
  return render(request,'login.html',locals())

#登出
from django.contrib.sessions.models import Session  
def logout(request):
  if 'username' in request.session: 
    Session.objects.all().delete()
    return redirect('/login/')
  return redirect('/')

#使用者資訊
def userinfo(request):
  if 'username' in request.session: 
    username  = request.session['username']
  else:
    return redirect('/login/')
  try:
    userinfo = models.User.objects.get(name=username) #抓資料庫資訊
  except:
    pass
  return render(request, 'userinfo.html',locals())