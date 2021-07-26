from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=200)
  slug  = models.CharField(max_length=200)
  body  = models.TextField()
  pub_date = models.DateTimeField(default=timezone.now)

  # 預設排序(可有可無)
  class Meta:  
    ordering = ('-pub_date',)#  用新增日期排序-表示倒序
    

  def __str__(self):
    return self.title  #在資料裡顯示title 可以改變其他的