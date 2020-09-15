from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic


from .models import *
from .forms import *


def tasks(request):
    era = Era.objects.all()
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo/')


    context = { 'tasks':tasks , 'form':form, 'era':era }
    return render(request, 'todo/todo.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/todo/')

    context = {'form':form}

    return render(request, 'todo/update.html', context)

def create_task(request):
    task = Task.objects.all()
    form = TaskForm()

    context = {'form':form, 'task':task}
    return render(request, 'todo/create.html', context)

def task_delete(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/todo/')

    context = {'item':item}
    return render(request, 'todo/delete.html', context)
