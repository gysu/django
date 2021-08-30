from django import forms #引入django的forms模組 
from . import models  #使用ModelForm要引入models
from captcha.fields import CaptchaField #機器人驗證

class ContactForm(forms.Form): #繼承forms.Form建立一個網站要使用的自訂表單類別
  CITY = [
    ['TP','Taipei'],
    ['TY','Taoyuang'],
    ['TC','Taichung'],
    ['TN','Tainan'],
    ['KS','Kaohsiung'],
    ['NA','Others'],
  ]
  user_name = forms.CharField(label="姓名",max_length=50,initial='小智',widget=forms.TextInput(attrs={'class':'form-control'}))
  user_city = forms.ChoiceField(label="居住城市",choices=CITY,widget=forms.Select(attrs={'class':'form-control'}))
  user_school =forms.BooleanField(label="是否在學",required=False) #預設值
  user_email = forms.EmailField(label="電子郵件",widget=forms.TextInput(attrs={'class': 'form-control'})) #自動驗證email
  user_message = forms.CharField(label="意見",widget=forms.Textarea(attrs={'class': 'form-control'})) #訊息框
  
 
'''
  # user_name = forms.CharField(label="姓名",max_length=50,initial='小智')
  # user_choice = forms.ChoiceField(label="居住城市",choices=CITY)
  # user_school =forms.BooleanField(label="是否在學",required=False) #預設值是否要有值
  # user_email = forms.EmailField(label="電子郵件") #自動驗證email
  # user_message = forms.CharField(label="意見") #訊息框
 
  # #這個方式也可以修改屬性attrs(全改)'class': 'form-control'
  # def __init__(self, *args, **kwargs):
  #     super(ContactForm, self).__init__(*args, **kwargs)
  #     for field in iter(self.fields):
  #         self.fields[field].widget.attrs.update({
  #             'class': 'form-control'
  #     })
#套用bootstrap https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
#都要給客製化的 class="form-contol"
#widget=forms.Textarea(attrs={'class': 'form-control'})
'''
#--------分隔線------
'''
class Meta:
        model = models.User     #關聯的model類
        fields = "__all__"      #或(‘name‘,‘email‘,‘user_type‘)    #驗證哪些字段，"__all__"表示所有字段
        exclude = None          #排除的字段
        labels = None           #提示信息
        help_texts = None       #幫助提示信息
        widgets = None          #自定義插件
        error_messages = None   #自定義錯誤信息（整體錯誤信息from django.core.exceptions import NON_FIELD_ERRORS）
        field_classes = None    #自定義字段類（也闊以自定義字段）
        localized_fields = ()   #本地化，根據settings中TIME_ZONE設置的不同時區顯示時間
'''
class PostForm(forms.ModelForm):
  captcha = CaptchaField()  #機器人驗證
  
  class Meta:
    model = models.Post
    fields = ['mood','nickname','message','del_pass'] #要顯示驗證哪些字段
   
  def __init__(self, *args, **kwargs):  #建構式改欄位名子
    super(PostForm,self).__init__(*args, **kwargs)
    self.fields['mood'].label="現在心情"
    self.fields['nickname'].label="暱稱"
    self.fields['message'].label="留言內容"
    self.fields['del_pass'].label="設定密碼"
    self.fields['captcha'].label="你是機器人"


# 建立Login表單使用Form
class LoginForm(forms.Form):
  username = forms.CharField(label='姓名',max_length=20)
  password = forms.CharField(label='密碼',widget=forms.PasswordInput())

#建立日記表單
class DateInput(forms.DateInput): #選日期DateInput
  input_type = 'date'

class DiaryForm(forms.ModelForm):
  class Meta:
    model=models.Diary
    fields = ['budget','weight','note','ddate']
    widgets={  #日期套件
      'ddate':DateInput(),
    }
  def __init__(self, *args, **kwargs):
    super(DiaryForm,self).__init__(*args, **kwargs)
    self.fields['budget'].label = '今日花費(元)'
    self.fields['weight'].label = '今日體重(KG)'
    self.fields['note'].label = '心情留言'
    self.fields['ddate'].label = '日期'
