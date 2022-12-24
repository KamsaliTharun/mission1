from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse("<h1>it is from app1 first fun</h1>")

def second(request):
    return HttpResponse("<h1>it is from app1 second fun</h1>")