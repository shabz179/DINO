from django.contrib import admin
from .models import Equipment
from .models import Bookinglog

# Register your models here.

admin.site.register(Equipment)
admin.site.register(Bookinglog)
