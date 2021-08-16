from django.db import models

# Create your models here.

class Maker(models.Model):
  name = models.CharField(max_length=20)
  country = models.CharField(max_length=20)
  def __str__(self):
    return self.name

class PModel(models.Model):
                 #ForeignKey參考Maker建立關聯, on_delete刪除時的狀態,ex:maker的資料刪除時Pmodel關聯maker的資料也會一併被刪除
  maker = models.ForeignKey(Maker,on_delete=models.CASCADE)
  name = models.CharField(max_length=40)
  url =models.URLField(default="http://i.imgur.com/Ous4iGB.png")

  def __str__(self):
    return self.name

class Product(models.Model):
  pmodel = models.ForeignKey(PModel,on_delete=models.CASCADE,verbose_name="型號")
  nickname = models.CharField(max_length=20,default="超值二手機",verbose_name="摘要")
  description = models.TextField(default="暫無說明",verbose_name="說明")
  year = models.PositiveIntegerField(default=0,verbose_name="使用幾年")
  price = models.PositiveIntegerField(default=3999,verbose_name="價格")
  
  def __str__(self):
    return self.nickname

class PPhoto(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  description = models.CharField(max_length=20,default="產品照片")
  url = models.URLField(default='http://i.imgur.com/Z230eeq.png')

  def __str__(self):
    return self.description