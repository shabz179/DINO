from django.urls import path
from .views import signup, admin_signup, user_dashboard, admin_dashboard
from . import views

urlpatterns = [

    path('user_signup/', signup, name='signup'),
    path('admin_signup/', admin_signup, name='admin_signup'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('create_booking/', views.create_booking, name='create_booking'),
]


