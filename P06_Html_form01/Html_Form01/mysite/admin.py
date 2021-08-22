from django.contrib import admin
from mysite import models
# Register your models here.

admin.site.register(models.Mood)

class PostAdmin(admin.ModelAdmin):
  list_display =('nickname','message','enabled','pub_time')
  ordering=('-pub_time',)  #注意!!!!要tuple所以後面要加一個逗號
admin.site.register(models.Post,PostAdmin)
