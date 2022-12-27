from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>this is my first view</h1>')

def second(requet):
    return HttpResponse('<h2>this is my second view</h2>')
