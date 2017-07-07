# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Todo, User
from .forms import TodoForm


def index(request):
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    context = {'todolist': todolist, 'finishtodos': finishtodos}
    return render(request, 'todolist.html', context)


def addtodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id='1')
            todo = form.cleaned_data['todo']
            priority = form.cleaned_data['priority']
            todo = Todo(user=user, todo=todo, priority=priority, flag=1)
            todo.save()
            return redirect('/')
            return render(request, 'add_todo.html', {'form': form})
    else:
        form = TodoForm()
        return render(request, 'add_todo.html', {'form': form})


def tododelete(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo:
        todo.delete()
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return redirect('/')
    return render(request, 'todolist.html', {'todo': todo, 'todolist': todolist, 'finishtodos': finishtodos})


def edittodo(request, id=''):
    if request.method == 'POST':
        todo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=todo, priority=priority, flag='1')
        todo.save()
        return redirect('/')
        return render(request, 'add_todo.html', {'todo': todo})
    else:
        todo = Todo.objects.get(id=id)
        return render(request, 'add_todo.html', {'todo': todo})


def finishtodo(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == 1:
        todo.flag = 0
        todo.save()
    return redirect('/')
    return render(request, 'todolist.html', {'todo': todo})


def backtodo(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == 0:
        todo.flag = 1
        todo.save()
    return redirect('/')
    return render(request, 'todolist.html', {'todo': todo})
