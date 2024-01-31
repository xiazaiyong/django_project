from django.contrib import admin
from .models import *
# Register your models here.
class goods_Admin(admin.ModelAdmin):#货品列表
    list_display = ['goods_text','num','price','display_tags','dispaly_category']#列表显示的条件
    search_fields = ['goods_text','num','price','notes','tag']#可用于搜索的关键字
    list_editable = ['num','price']#可编辑字段
    list_per_page = 20
    autocomplete_fields = ['tag','category']
    def display_tags(self, obj):
        return ",".join ([tag.tag_text for tag in obj.tag.all()])

    def dispaly_category(self, obj):
        return obj.category

    display_tags.short_description = "标签"
    dispaly_category.short_description = "分类"

class tag_Admin(admin.ModelAdmin):
    list_display = ['tag_text']
    search_fields = ['tag_text']

class categorize_Admin(admin.ModelAdmin):
    list_display = ['categorize_text']
    search_fields = ['categorize_text']

admin.site.register(goods,goods_Admin)
admin.site.register(categorize,categorize_Admin)
admin.site.register(tag,tag_Admin)
admin.site.register(brand)
admin.site.register(picture)