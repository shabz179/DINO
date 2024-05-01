from django.shortcuts import render
from .models import Equipment




# Create your views here.

def my_view(request):
    return render(request,'main.html')

def equipment_list(request):
    equipments = Equipment.objects.all()
    context = {'equipment': equipments} # type: ignore
    return render(request,'equipment.html', context)

def bookings(request):
    return render( request,'bookings.html')

