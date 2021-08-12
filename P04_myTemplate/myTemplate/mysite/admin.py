from django.contrib import admin
from mysite.models import car_table,tv_table
# Register your models here.

class CarAdmin(admin.ModelAdmin):
  list_display =("model","car_maker","price","qty")
admin.site.register(car_table,CarAdmin)

class TVAdmin(admin.ModelAdmin):
  list_display =("name","engname","tvcode")
admin.site.register(tv_table,TVAdmin)
