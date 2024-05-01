from django.contrib import admin
from .models import User, Booking

class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']  
    search_fields = ['firstname', 'lastname', 'email']

admin.site.register(User, UserAdmin)
admin.site.register(Booking)
