from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.db import IntegrityError
from .models import AdminUser
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 
from .models import EquipmentReservation, UserHistory, Item


def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Try to create a new User object and save it to the database
            new_user = User.objects.create(firstname=firstname, lastname=lastname, email=email, password=password)
            
            # Set success message
            message = "Account has been successfully created!"
            # Redirect to a success page or wherever you want
            return render(request, 'user_signup.html', {'message': message})

        except IntegrityError:
            # Handle the case where the email already exists in the database
            message = "Account already exists. Please use a different email."
            return render(request, 'user_signup.html', {'message': message})

    return render(request, 'user_signup.html')

def admin_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('admin_signup')
        
        try:
            # Check if the email already exists
            if get_user_model().objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('admin_signup')
            
            # Create the user
            user = get_user_model().objects.create_user(username=username, email=email, password=password)
            
            # Set success message
            messages.success(request, "Account has been successfully created!")
            
            # Redirect to a different URL after successful creation
            return redirect('admin_signup')  # Assuming you want to stay on the admin signup page after successful creation
        
        except IntegrityError:
            # Handle the case where the email already exists in the database
            message = "Account already exists. Please use a different email."
            return render(request, 'admin_signup.html', {'message': message})
        
    return render(request, 'admin_signup.html')

@login_required
def user_dashboard(request):
    # Retrieve data for the user dashboard
    equipment_history = EquipmentReservation.objects.filter(user=request.user)
    user_history = UserHistory.objects.filter(user=request.user)
    items = Item.objects.all()
    
    # Render the dashboard template with the retrieved data
    return render(request, 'dashboard.html', {
        'equipment_history': equipment_history,
        'user_history': user_history,
        'items': items,
    })

@login_required
def admin_dashboard(request):
    # Retrieve data for the user dashboard
    equipment_history = EquipmentReservation.objects.filter(user=request.user)
    user_history = UserHistory.objects.filter(user=request.user)
    items = Item.objects.all()
    
    # Render the dashboard template with the retrieved data
    return render(request, 'dashboard.html', {
        'equipment_history': equipment_history,
        'user_history': user_history,
        'items': items,
    })

def create_booking(request):
    if request.method == 'POST':
        # Handle form submission
        item = request.POST.get('item')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        duration = request.POST.get('duration')
        
        # Perform validation and database operations as needed
        
        # For now, just returning a success message
        return HttpResponse("Booking created successfully.")
    else:
        # Render the form template
        return render(request, 'create_booking.html')
