from django.shortcuts import render

# Create your views here.
from mysite import models

def index(request):
  products = models.Product.objects.all()

  return render(request, 'index.html',locals())

def detail(request,no):
  # print(no)
  try:
    prod = models.Product.objects.get(id =no)
    images = models.PPhoto.objects.filter(product = prod)
  except:
    pass 
  return render(request, 'detail.html',locals())
