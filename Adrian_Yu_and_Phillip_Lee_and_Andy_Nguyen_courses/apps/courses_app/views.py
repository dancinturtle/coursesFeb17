from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Description

def index(request):
    context = {
    "courses" : Course.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def process(request):
    Description.objects.create(description=request.POST['description'], course_id = Course.objects.create(name=request.POST['name']))
    return redirect('/')

def confirm(request, id):
    holder = {
        "course_info" : Course.objects.get(id=id)
    }
    return render(request, "courses_app/confirm.html", holder)

def confirmed(request, id):
    ids = Course.objects.get(id=id).delete()
    return redirect("/")
