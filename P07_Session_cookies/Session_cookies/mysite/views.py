from mysite.forms import PostForm
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from mysite import models
from mysite import forms

#第三方寄信
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


#使用django內建的登入方式
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages



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

  # if 'username' in request.session:       
  #   username = request.session['username']
  #   usermail = request.session['useremail']



#使用內建的user就不用再從session中撈使用者資料簡化寫法
  if request.user.is_authenticated:#使用is_authenticated來檢查使用者是否有登入
    username = request.user.username
  messages.get_messages(request)

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

#驗證
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

'''
#登入  session 的用法
#Message Framework運用
from django.contrib import messages
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
            messages.add_message(request,messages.SUCCESS,'成功登入了') 
            return redirect('/userinfo/')
          else:
            # message = "密碼錯誤"
            messages.add_message(request,messages.WARNING,'密碼錯誤,請檢查') 

       except:
          # message = "找不到使用者"
            messages.add_message(request,messages.WARNING,'找不到使用者') 

  else:
    login_form = forms.LoginForm()
    messages.add_message(request,messages.INFO,'請檢查輸入的欄位內容') 

  return render(request,'login.html',locals())
#-----------
#登出
from django.contrib.sessions.models import Session  
def logout(request):
  if 'username' in request.session: 
    Session.objects.all().delete()
    return redirect('/login/')
  return redirect('/')
'''

#--------------

#使用者資訊
@login_required(login_url='/login/') #裝飾器 沒登入就重導到login頁面
def userinfo(request):
  #這是用session
  # if 'username' in request.session: 
  #   username  = request.session['username']
  #這是用內建auth
  if request.user.is_authenticated:   #如果有登入
    username  = request.user.username #從內建user資料撈出username欄位
    print(username)
  else:
    return redirect('/login/')
  try:
    # userinfo = models.User.objects.get(name=username) #抓資料庫資訊
    user = User.objects.get(username=username) #抓資料庫資訊
    userinfo = models.Profile.objects.get(user=user)
    print('123',username,userinfo)
  except:
    pass
  return render(request, 'userinfo.html',locals())

'''
#使用內建的user驗證 登入登出功能

from django.contrib.auth.models import User

user = User.objects.create_user('pikachu','pikachu@ntu.edu.tw', 'pikachu')

user.last_name = 'Pokemon' #修改其中的任一欄位資料
user.save()
'''

#--------------

#使用django內建的登入方式
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
  if request.method == 'POST':
     login_form = forms.LoginForm(request.POST) 
     if login_form.is_valid():                       
       login_name = request.POST['username'].strip() #從表單中取得的login_name和login_password
       login_password = request.POST['password'] 
       user = authenticate(username = login_name ,password=login_password) # 透過authenticate進行驗證的工作
       if user is not None:  #驗證成功此函數會傳回該使用者的資料放在user變數,驗證失敗則回傳None
         if user.is_active: #成功登入之後可以再使用user.is_active來檢查此帳號是否有效
           auth.login(request,user) #如果一切都通過，使用auth.login(request, user)把此使用者的資料存入Session中，供接下來其它網頁中使用
           print("success",user)
           messages.add_message(request,messages.SUCCESS,'登入成功')
           return redirect('/userinfo/')
         else:
           messages.add_message(request,messages.WARNING,'帳號尚未啟用')
       else:
           messages.add_message(request,messages.WARNING,'登入失敗')
     else:
           messages.add_message(request,messages.INFO,'請檢查輸入的欄位內容')

  else:
    login_form = forms.LoginForm()

  return render(request,'login.html',locals())

#--------------

#使用django內建的登出方式
def logout(request):
  auth.logout(request)
  messages.add_message(request, messages.INFO, "成功登出了")
  return redirect('/login/')

#--------------

##Diary日記
def diary(request): #從資料庫產生的form 再從
  if request.method == "POST":
    diary_form = forms.DiaryForm(request.POST)
    if diary_form.is_valid():   #檢查DOM裡的資料是否正確
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
      ur_pass = diary_form.cleaned_data.get('del_pass') #取得樣板所填寫的資料
      
      if request.user.is_authenticated:              #如股有登入
        username = request.user.username             #從內建user資料撈出username欄位
        user = User.objects.get(username=username)   #抓user資料
        diary = models.Diary(user=user)              #將user資訊丟給diary user 因為要寫入資料庫缺使用者
        print(diary,'123')
        diary_form = forms.DiaryForm(request.POST, instance=diary)
        print(diary_form,'456')
      if result['success']:#google驗證
         messages.add_message(request, messages.INFO, "日記已儲存")
         diary_form.save()
        # else:
          # message="您的訊息已發布。"
          # print(message)
          # new = diary_form.save(commit=False)  #先把這筆記錄commit起來
          # new.enabled = True                  #可以改其他欄位
          # new.save()                          #再儲存
          # diary_form.save()            #儲存後畫面不會跳轉
         return redirect('/list/')#所以重導畫面
      else:
        messages.add_message(request, messages.WARNING, "reCAPTCHA驗證失敗，請在確認")
        # message = "reCAPTCHA驗證失敗，請在確認."
    else:
      messages.add_message(request, messages.WARNING, "每個欄位都須填寫")

      # message = '每個欄位都須填寫'
  else:
    diary_form = forms.DiaryForm() #從form.py
    moods = models.Mood.objects.all()
    messages.add_message(request, messages.WARNING, "每個欄位都須填寫")
    # message = '每個欄位都須填寫'
  return render(request,'diary.html',locals())



#負責顯示日記
def diary_list(request,):
  if request.user.is_authenticated: #判斷使用者有沒有登入
    username = request.user.username
    useremail = request.user.email
    try:
      user = User.objects.get(username=username)
      
      diaries = models.Diary.objects.filter(user=user).order_by('-ddate')
      print(diaries,'123')
    except:
      pass
  return render(request,"diary_list.html", locals())



#刪除日記
def diary_del(request,pid=None):
  if request.user.is_authenticated: #判斷使用者有沒有登入
    if pid:
      try:
        diary = models.Diary.objects.get(id=pid)
      except:
        diary =None
      if diary != None:
        diary.delete()
        message = "資料刪除成功"
      else:
        message = "密碼錯誤"
    return redirect('/diary_list/')
