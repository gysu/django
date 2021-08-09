from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
import random
from django.http import Http404
# Create your views here.
def MTVhome(request):
  quotes =['有所資本加強改進是不是釣魚幹部活動有限責任公司，看過玄幻儘。',
           '麻煩表現精品次數事故痛苦，如此全家，推。',
           '一會兒手段無線說過才是最大美元，證據防止細節高級。',
           '完了出來呵呵吃螺絲歡迎您，畢業。'] 
  quote = random.choice(quotes)
  return render(request,'MTVhome.html',locals())

def about(request):
  quotes =['有所資本加強改進是不是釣魚幹部活動有限責任公司，看過玄幻儘。',
           '麻煩表現精品次數事故痛苦，如此全家，推。',
           '一會兒手段無線說過才是最大美元，證據防止細節高級。',
           '完了出來呵呵吃螺絲歡迎您，畢業。'] 
  quote = random.choice(quotes)
  return render(request,'about.html',locals())
 
def listing(request):
  products = Product.objects.all().exclude(qty=0) #庫存
  products2 = Product.objects.all().filter(qty=0) #庫存=0

  return render(request,'list.html',locals())

#直接用view顯示到畫面  不建議
def disp_detail(request,sku):
  try:
    p=Product.objects.get(sku=sku )
  except:
    raise Http404('找不到指定的品項編號')

  return render(request,'detail.html',locals())
 
  #第一種 回傳HttpResponse
  # html='hello66'
  # return HttpResponse(html)
  #第二種 告訴view 渲染about畫面 帶入那些資料
  # content={'aa':'hello'}
  # return render(request,'about.html',content)
  #第三種
#   html ='''<html><head><title>about</title></head>
#         <body>   
#         <h2>直接顯示資料到網頁的步驟是 </h2> 
#         <p>在views.py中編寫一個函數，透過HttpResponse傳遞出想要顯示
# 的資料</p>
#         </body>
#         </html>    
#         '''





def listing2(request):
  html ='''<html><head><title>資料列表</title></head>
        <body>   
        <h2>直接顯示資料到網頁的listing </h2> 
        <p>庫存列表</p>
        <hr>
        <table width=400 border=1 bgcolor='#ccffcc'>
        {}    
        </table>
        <p>以下是缺貨</p>
        <table width=400 border=1 bgcolor='#ccffcc'>
        {}    
        </table>
        </body>
        </html>    
        '''
  products = Product.objects.all().order_by('-price').exclude(qty=0) #排序排除庫存=0
  tags = '''<tr><td>品名</td>   <td>售價</td>  <td>庫存量</td>  </tr>'''
  for p in products:
    tags = tags + '<tr><td>{}</td>'.format(p.name)
    tags = tags + '<td>{}</td>'.format(p.price)
    tags = tags + '<td>{}</td></tr>'.format(p.qty)

  products2 = Product.objects.all().order_by('-name').filter(qty=0) #只找庫存=0
  tags2 = '''<tr><td>品名</td>  <td>售價</td>  <td>庫存量</td>   </tr>'''
  for p in products2:
    tags2 = tags2 + '<tr><td>{}</td>'.format(p.name)
    tags2 = tags2 + '<td>{}</td>'.format(p.price)
    tags2 = tags2 + '<td>{}</td></tr>'.format(p.qty)
  return HttpResponse(html.format(tags,tags2))

