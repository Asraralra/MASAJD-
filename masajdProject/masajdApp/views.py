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
        new_problem = problem(mosque_name=request.POST["mosque_name"],city = request.POST["city"] , location=request.POST["location"] , PhoneNum= request.POST["PhoneNum"] , Description=request.POST["Description"], image= request.FILES["image"] )
        new_problem.save()

    return render(request, "masajdApp/add_problem.html", {"problem" : problem, "problemForm": ProblemForm()})



def all_problems (request: HttpRequest):
   problems = problem.objects.all()
   return render(request, "masajdApp/view_problems.html" , {"problems": problems})



def problem_detail(request : HttpRequest, problem_id : int):

    try:
        problem = problem.objects.get(id= problem_id )
    except:
        return render(request , "masajdApp/not_found.html")

    return render(request, "masajdApp/problem_detail.html", {"problem" : problem })



def update_problem (request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "masajdApp/not_found.html")

    if request.method== "Post":
       problem.mosque_name= request.POST["mosque_name"]
       problem.city = request.POST["city"]
       problem.location=request.POST["location"]
       problem.PhoneNum= request.POST["PhoneNum"]
       problem.Description=request.POST["Description"]
       problem.image= request.FILES["image"] 
       problem.save()

       return redirect("masajdApp:all_problems")

    
    return render(request, "masajdApp/update_problem.html", {"problem" : problem})




def delete_problem (request: HttpRequest, problem_id :int):

    try:
        post = problem.objects.get(id= problem_id)
    except:
        return render(request , "masajdApp/not_found.html")

    problem.delete() 

    return redirect("masajdApp:all_problems")


