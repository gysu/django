from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
   return HttpResponse("hello new Url project")
def about(request,author_no=0): #預設參數=0 about/後面沒有加東西時導到預設值
  html = "<h2> Here is No:{}'s about page </h2> <hr> ".format(author_no)
  return HttpResponse(html)


def company(request):
  return HttpResponse("my company")
def sales(request):
  return HttpResponse("my sales")
def contact(request):
  return HttpResponse("my contact")