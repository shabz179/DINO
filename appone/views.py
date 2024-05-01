from django.shortcuts import render
from account.models import Account 



# Create your views here.

def about(request):
    return render(request, 'about.html')    

def home(request):
    return render(request, 'base.html')     



