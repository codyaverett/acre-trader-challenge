from django.shortcuts import render
from ..models import Todo, TodoList


def home(request):
    return render(request, 'home.html', {
        'todos': Todo.objects.all(),
        'todo_lists': TodoList.objects.all(),
    })
