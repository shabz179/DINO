from django.shortcuts import render
from .models import Equipment
from django.http import HttpResponse
from .models import Bookinglog

# Create your views here.

def my_view(request):
    return render(request,'main.html')

def equipment_list(request):
    equipments = Equipment.objects.all()
    context = {'equipment': equipments} # type: ignore
    return render(request,'equipment.html', context)

def create_booking(request):
    if request.method == 'POST':
        # Handle form submission
        item = request.POST.get('item')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        duration = request.POST.get('duration')

        booking = Bookinglog.objects.create(
            item = item,
            start_date= start_date,
            end_date = end_date,
            duration = duration,
            user = request.user
        )
        
        Bookinglog.objects.create(user = request.user, booking = booking)
        # Perform validation and database operations as needed
        
        # For now, just returning a success message
        return HttpResponse("Booking created successfully.")
    else:
        # Render the form template
        return render(request, 'bookings.html')
    
def booking_log(request):
    booking_log = Bookinglog.objects.all()
    return render(request, 'bookinglogs.html', {'booking_log': booking_log})