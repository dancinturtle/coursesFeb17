from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def home(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'add_course/home.html', context)

def add(request):
 # using ORM
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
 # insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
    return redirect('/')

def renderDelete(request, id):
    this_course = Course.objects.get(id=id)
    context = {
        'this_course': this_course
    }

    return render(request, 'add_course/delete.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
