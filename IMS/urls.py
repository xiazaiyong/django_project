from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='IMS_Index'),
    path('passwordmanagement', views.password_management, name='pwdmanagement'),
    
]