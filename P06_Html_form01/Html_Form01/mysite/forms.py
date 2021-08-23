from django import forms #引入django的forms模組 

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
 
 
 ##############
  # user_name = forms.CharField(label="姓名",max_length=50,initial='小智')
  # user_choice = forms.ChoiceField(label="居住城市",choices=CITY)
  # user_school =forms.BooleanField(label="是否在學",required=False) #預設值
  # user_email = forms.EmailField(label="電子郵件") #自動驗證email
  # user_message = forms.CharField(label="意見") #訊息框
 
  # #這個方式也可以修改(全改)'class': 'form-control'
  # def __init__(self, *args, **kwargs):
  #     super(ContactForm, self).__init__(*args, **kwargs)
  #     for field in iter(self.fields):
  #         self.fields[field].widget.attrs.update({
  #             'class': 'form-control'
  #     })
#套用bootstrap https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
#都要給客製化的 class="form-contol"
#widget=forms.Textarea(attrs={'class': 'form-control'})
###########
  