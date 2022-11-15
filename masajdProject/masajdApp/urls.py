from django.urls import path
from . import views

app_name = "masajdApp"

urlpatterns = [
    path("home/", views.home_page, name="home"),


]