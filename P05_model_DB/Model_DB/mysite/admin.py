from django.contrib import admin

# Register your models here.
from mysite import models


class MakerAdmin(admin.ModelAdmin):
  list_display =("name","country")
class PModelAdmin(admin.ModelAdmin):
  list_display =("maker","name","url")
class ProductAdmin(admin.ModelAdmin):
  list_display =("pmodel","nickname","description","year","price")
  search_fields =('nickname','description')
  ordering=('-price',)
class PPhotoAdmin(admin.ModelAdmin):
  list_display =("product","description","url")
admin.site.register(models.Maker,MakerAdmin)
admin.site.register(models.PModel,PModelAdmin)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.PPhoto,PPhotoAdmin)