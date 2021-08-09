from django.contrib import admin
from mysite.models import NewTable,Product
# Register your models here.
admin.site.register(NewTable)

class ProductAdmin(admin.ModelAdmin):
  list_display =("name","price","qty","size")

admin.site.register(Product,ProductAdmin)

