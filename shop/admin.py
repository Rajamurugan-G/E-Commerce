from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','product_image','vendor')

admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Product,ProductAdmin)