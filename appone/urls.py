from . import views
from django.urls import path 

from account.views import (
    registration_view,
    logout_view,
    login_view

) 

urlpatterns = [
    path('',views.home, name="home"),
    path('about/', views.about, name="about"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/' , login_view, name="login"),
    
 
]
