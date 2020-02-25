from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HelloDjango(TemplateView): #继承了templateView 的所有方法
    template_name = 'test.html' #要在templates里