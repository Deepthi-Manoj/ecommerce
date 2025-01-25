from django.contrib import admin
from . models import *

# Register your models here.

class SubcategoryTabular(admin.TabularInline):
    model= Sub_Category

class CategoryAdmin(admin.ModelAdmin):
    inlines=[SubcategoryTabular]

class AdditionalinfoTabular(admin.TabularInline) :
    model = Additional_information
class AdditionalimageTabular(admin.TabularInline) :
    model = Additional_image

class ProductAdmin(admin.ModelAdmin)  :
    inlines = [AdditionalinfoTabular,AdditionalimageTabular] 



admin.site.register(Banner_area)
admin.site.register(Main_Category)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Banner)
admin.site.register(Product,ProductAdmin)
