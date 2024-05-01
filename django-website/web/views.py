from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def about_us(request):
    return render(
        request,
        'about_us.html',
        {}
    )