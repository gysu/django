from django.db import models

# Create your models here.
class NewTable(models.Model):
  models_f = models.BigIntegerField()
  bool_f =models.BooleanField()
  date_f = models.DateField(auto_now=True)
  char_f =models.CharField(max_length=20,unique=True)
  datetime_f = models.DateField(auto_now_add=True)
  decimal_f = models.DecimalField(max_digits=10,decimal_places=2)
  float_f =models.FloatField(null=True)
  int_f = models.IntegerField(default=2010)
  tesxt_f=models.TextField()

class Product(models.Model):
  SIZES=(                #選單內容
    ('S','Small'),
    ('M','Medium'),
    ('L','Large'),
  )
  sku = models.CharField(max_length=5)  #短網址
  name = models.CharField(max_length=20) #品名
  price =models.PositiveIntegerField()
  qty  = models.IntegerField(default=0)
  size = models.CharField(max_length=1,choices=SIZES) #下拉選單
  
  def __str__(self):
    return self.name  #在admin資料裡顯示name 可以改變其他的