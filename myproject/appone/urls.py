from . import views
from django.urls import path


urlpatterns = [
    path('',views.home),
    path('blist/',views.blist),
    path('reserve/', views.reserve),
]