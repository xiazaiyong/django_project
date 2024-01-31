from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    goods_list = goods.objects.all().order_by('id')
    invements = {
        "goods_list":goods_list,
    }
    #print(goods_list.tag.all())
    return render(request, 'index.html',invements)

def password_management(request):
    
    return render(request, 'passwordmanagement.html')