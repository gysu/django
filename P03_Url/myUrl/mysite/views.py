from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
  return HttpResponse("new project url")
def about(request,author_no=0): #預設參數=0 about/後面沒有加東西時導到預設值
  html = "<h2> Here is No:{}'s about page </h2> <hr> ".format(author_no)
  return HttpResponse(html)


def company(request):
  return HttpResponse("my company")
def sales(request):
  return HttpResponse("my sales")
def contact(request):
  return HttpResponse("my contact")

def listing(request,yr,mon,day):
  html ="<h2>Your List Date is {}/{}/{}</h2> <hr>".format(yr,mon,day)
  return HttpResponse(html)
def post(request,yr,mon,day,post_num):
  html="<h2>Today is {}/{}/{}:Your Post Number:{}</h2>".format(yr,mon,day,post_num)
  return HttpResponse(html)
def homepage(request):
  year = 2021
  month= 8
  day =9
  postid=3
  html="<a href='post/{}/{}/{}/{}'> show the post  </a>".format(year,month,day,postid)
  return HttpResponse(html)