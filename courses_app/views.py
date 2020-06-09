from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def main(request):
    context={
        "all_courses": Course.objects.all()
    }

    if request.method=="POST":

        errors = Course.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/courses/")

        else:
            Course.objects.create(name=request.POST['name'], description=request.POST['description'])
            return redirect("/courses/")

    return render(request, 'main.html', context)

def delete(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)

def no(request):
    return redirect("/courses/")

def yes(request,id):
    m = Course.objects.get(id=id)
    m.delete()
    return redirect("/courses/")