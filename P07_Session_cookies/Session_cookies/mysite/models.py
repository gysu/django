from django.db import models
# Create your models here.


class Mood(models.Model):
  status = models.CharField(max_length=20,null = False) #文字欄位 記錄心情

  def __str__(self):
    return self.status

class Post(models.Model):
  mood = models.ForeignKey(Mood,on_delete=models.CASCADE)
  nickname = models.CharField(max_length=50,default='請輸入暱稱') 
  message  = models.TextField(null=False) 
  del_pass = models.CharField(max_length=50,blank=True) #blank=True ModelForm不用驗證也可以
  pub_time = models.DateTimeField(auto_now=True)
  enabled  = models.BooleanField(default=False) #改True 就可以預設開啟
                                                #是否要把這筆資料顯示到網頁上
  def __str__(self):
    return self.message
    
##session登入資訊 與內建auth.user衝突 先註解調 
# class User(models.Model):
#   name = models.CharField(max_length=20,null=False)
#   email = models.EmailField()
#   password = models.CharField(max_length=20,null =False)
#   enabled = models.BooleanField(default=False)
#   def __str__(self):
#     return self.name

##擴充user資料欄位
from django.contrib.auth.models import User
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  height = models.PositiveIntegerField(default=160)
  male = models.BooleanField(default=False)
  website=models.URLField(null=True)
  def __str__(self):
    return self.user.username

####建立日記資料表
class Diary(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  budget = models.FloatField(default=0)
  weight = models.FloatField(default=0)
  note = models.TextField()
  ddate = models.DateField()

  def __str__(self):
    return "{}({})".format(self.ddate, self.user)
