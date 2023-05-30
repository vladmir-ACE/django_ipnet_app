from django.shortcuts import render

# Create your views here.
from  django.http import  HttpResponse

def hello(request):
    noms=['VLAD','KING','ACE']
    return render(request,'blog/hello.html',{'anne_academique':'2022-2023','noms':noms})

def about(request):
    return render(request,'blog/about.html')


