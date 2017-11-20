from django.contrib import admin
from .models import Users,SaleD,ShopList

class UserList(admin.ModelAdmin):
    list_display = ('name','password')

class SaleList(admin.ModelAdmin):
    list_display = ('Gapple','Gorange','Gbowl','Gchopstick','Grag','Gtissue','Gnoddle','Gham', 'Gdate')

admin.site.register(Users,UserList)
admin.site.register(SaleD,SaleList)
admin.site.register(ShopList)