from django.urls import path
from . import views

urlpatterns = [
    path('home/' , views.home),
    path('blist/', views.blist),
    path('Equipment/', views.Equipment)
]