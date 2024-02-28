from django.db import models
from enum import Enum
from django.utils.html import format_html
# Create your models here.

class categorize(models.Model):#分类表
    id = models.BigAutoField(primary_key = True)#id
    categorize_text = models.CharField(max_length = 100, verbose_name = '分类')#分类名称
    
    def __str__(self):
        return self.categorize_text
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        db_table = 'categorize'

class tag(models.Model):#标签表
    id = models.BigAutoField(primary_key = True)#id
    tag_text = models.CharField(max_length = 100, verbose_name = '标签', blank = True, null = False)#标签
    
    def __str__(self):
        return self.tag_text
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        db_table = 'tag'

class brand(models.Model):#品牌表
    id = models.BigAutoField(primary_key = True)#id
    brand_name = models.CharField(max_length = 100, verbose_name = '品牌名称', blank = True, null = False)#品牌名称
    
    def __str__(self):
        return self.brand_name
    
    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name
        db_table = 'brand'

class picture(models.Model):#图片表
    id = models.BigAutoField(primary_key = True)#id
    picture_name = models.CharField(max_length = 20, verbose_name = '图片名称', blank = True, null = False)#图片名称

    def Carousel_pic_preview(self):
        if self.pic:
            return format_html('<img src="/media/{}" height="70px"/>',self.pic,)

    def __str__(self):
        return self.picture_name
    
    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name
        db_table = 'pictures'

class goods(models.Model):#货品表
    id = models.BigAutoField(primary_key = True)#id
    goods_text = models.CharField(max_length = 50, verbose_name = '货品名称', blank = True, null = False)#货品名称
    goods_brand = models.ManyToManyField(to = brand, verbose_name = '品牌', blank = True,)#货品品牌
    picture = models.ManyToManyField(picture, verbose_name = '图片', blank = True)#图片
    bar_code = models.BigIntegerField(default = 0 ,verbose_name = '条形码数据')#条形码数据
    category = models.ForeignKey(categorize, verbose_name = '分类', on_delete = models.SET_NULL, blank = True, null = True,
                                 related_name = 'sorting')#分类
    num = models.IntegerField(default = 0, verbose_name = '数量', blank = True, null = False)#数量
    price = models.CharField(max_length = 100, verbose_name = '价格', blank = True, null = False)#价格
    tag = models.ManyToManyField(tag, related_name= 'Tag',verbose_name = '标签', blank = True)#标签
    notes = models.CharField(max_length = 300, verbose_name = '备注', blank = True, null = True)#备注

    def __str__(self):
        return self.goods_text
    
    class Meta:
        verbose_name = '货品'
        verbose_name_plural = verbose_name
        db_table = 'invent'