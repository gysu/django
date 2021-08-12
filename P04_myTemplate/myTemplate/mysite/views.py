from django.shortcuts import render
from datetime import datetime
from .models import car_table,tv_table
# Create your views here.

def index(request,tvno=0):
  # tv_list =[{'name':'東森','tvcode':'3itCt5qiB0E'},
  #           {'name':'民視','tvcode':'XxJKnDLYZz4'},
  #           {'name':'台視','tvcode':'X67BgdUEwKw'},
  #           {'name':'華視','tvcode':'-uuU63KiErs'}]
  tv_list = tv_table.objects.all()
  now = datetime.now()
  tvno =tvno
  tv=tv_list[tvno]
  hour = now.timetuple().tm_hour
  return render(request,'index.html',locals())

def yt(request,tvno=0): #預設0
  # tv_list =[{'name':'東森','tvcode':'3itCt5qiB0E'},
  #           {'name':'民視','tvcode':'XxJKnDLYZz4'},
  #           {'name':'台視','tvcode':'X67BgdUEwKw'},
  #           {'name':'華視','tvcode':'-uuU63KiErs'}]
  tv_list = tv_table.objects.all()
  now = datetime.now()
  tvno =tvno 
  tv=tv_list[tvno]
  hour = now.timetuple().tm_hour
  return render(request,'index.html',locals())

def engyt(request,tvno=0): #預設0
  # tv_list =[{'name':'EBC','tvcode':'3itCt5qiB0E'},
  #           {'name':'FTV','tvcode':'XxJKnDLYZz4'},
  #           {'name':'CCTV','tvcode':'X67BgdUEwKw'},
  #           {'name':'TTV','tvcode':'-uuU63KiErs'}]
  tv_list = tv_table.objects.all()
  now = datetime.now()
  hour = now.timetuple().tm_hour
  tvno =tvno 
  tv=tv_list[tvno]
  return render(request,'engindex.html',locals())

def carlist(request,maker=0):  #預設0
  car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
  # car_list=[ [],
  #             ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
  #             ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
  #             ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
  #             ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
  #             ['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish'],
  #          ]
  # car_list=[[],
  #          [{'model':'Fiesta','price':3999,'qty':3}, {'model':'Focus','price':46666,'qty':8}],
  #          [{'model':'Fit','price':5999,'qty':2},{'model': 'Odyssey','price':6999,'qty':9},{ 'model':'CR-V', 'price':7999,'qty':11},{'model':'City','price':8999,'qty':5},{ 'model':'NSX','price':9999,'qty':3}],
  #          [{'model':'Mazda3','price':123,'qty':3}, {'model':'Mazda5','price':321,'qty':0}],
  #          [{'model':'tidda','price':123,'qty':3}],
  #          [{'model':'86','price':1123,'qty':8}],           
  #          ]
  car_list = car_table.objects.filter(car_maker=maker)
  # car_makers =car_table.makers
  maker_name = car_maker[maker]
  cars =car_list
  print(cars)
  return render(request,'car.html',locals())