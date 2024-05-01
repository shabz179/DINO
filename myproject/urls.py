"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from juhaerapp import views
from juhaerapp.views import my_view
from django.conf.urls.static import static 
from django.conf import settings
from juhaerapp.views import equipment_list 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view, name='main'),
    path('equipment/', equipment_list, name='equipment_list'),
    path('bookings/', views.bookings, name='bookings'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
 