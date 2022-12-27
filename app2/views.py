from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ashok(request):
    return HttpResponse('<h1>this is first view ashok</h1>')

def aravind(request):
    return HttpResponse('<h2>ashok is my brother</h2>')
