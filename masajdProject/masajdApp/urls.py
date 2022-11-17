from django.urls import path
from . import views

app_name = "masajdApp"

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("add/problem", views.add_problem , name="add_problem "),
    path("view/problem", views.all_problems , name="all_problems"),
    path("problem/detail/<problem_id>/", views.problem_detail, name="problem_detail"),


]