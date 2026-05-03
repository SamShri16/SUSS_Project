from django.shortcuts import render, redirect
from .models import Task

def planner(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'planner.html', {'tasks': tasks})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/planner/')


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/planner/')