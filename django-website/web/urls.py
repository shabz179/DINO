from django.urls import path
from web import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us", views.about_us, name="about_us"),
]