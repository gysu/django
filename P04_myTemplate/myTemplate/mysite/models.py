from django.db import models
from django.utils import timezone
# Create your models here.

class car_table(models.Model):
  makers = [('0','SAAB'), 
           ('1','Ford'),
           ('2','Honda'), 
           ('3','Mazda'),
           ('4','Nissan'),
           ('5','Toyota') ]
  car_maker=models.CharField(max_length=20,choices=makers)
  model =models.CharField(max_length=20,unique=True)
  price = models.IntegerField()
  qty = models.IntegerField()
  date = models.DateField(auto_now=True)

  def __str__(self):
   return self.model  #在admin資料裡顯示model 可以改變其他的

class tv_table(models.Model):
  name = models.CharField(max_length=20)
  engname = models.CharField(max_length=20)
  tvcode = models.CharField(max_length=20)
  
  def __str__(self):
   return self.name  #在admin資料裡顯示name 可以改變其他的
