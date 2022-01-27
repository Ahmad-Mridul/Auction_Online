from django.contrib import admin
from Core.models import *


# Register your models here.
class Categories(admin.ModelAdmin):
    list_display = ('slug', 'cat_name ', 'cat_img')
    admin.site.register(Categories)


class ProductData(admin.ModelAdmin):
    list_display = ('p_img', 'p_name', 'p_price', 'p_description', 'categories_name')
    admin.site.register(Product)


