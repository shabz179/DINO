from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello world</h1')

def blist(request):
    return HttpResponse('<h1>blist page</h1')

def reserve(request):
    return render(request, 'reserve.html')