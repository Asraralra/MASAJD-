from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse 
from .models import problem 
from django.forms import ModelForm

# Create your views here.

class ProblemForm(ModelForm):

    class Meta:
        model = problem
        fields = "__all__"

def home_page (request : HttpRequest):

     return render(request, "masajdApp/base.html") 



def add_problem (request : HttpRequest):
  
    if request.method == "POST":
        new_problem = problem(mosque_name=request.POST["mosque_name"],city = request.POST["city"] , location=request.POST["location"] , is_PhoneNum= request.POST["PhoneNum"] , Description=request.POST["Description"])
        new_problem.save()

    return render(request, "masajdApp/add_problem.html", {"problem" : problem, "problemForm": ProblemForm()})




