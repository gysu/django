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
    
##session登入資訊
class User(models.Model):
  name = models.CharField(max_length=20,null=False)
  email = models.EmailField()
  password = models.CharField(max_length=20,null =False)
  enabled = models.BooleanField(default=False)
  def __str__(self):
    return self.name
