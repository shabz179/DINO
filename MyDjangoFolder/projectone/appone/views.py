from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return HttpResponse('hello world')
def blist(request):
    return HttpResponse('blist page')
def Equipment(request):
    return render(request , 'Equipment.html')