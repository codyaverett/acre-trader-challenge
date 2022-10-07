from django.shortcuts import render
from ..models import Todo, TodoList


def app(request):
    return render(request, 'app.html', {
        'todos': Todo.objects.all(),
        'todo_lists': TodoList.objects.all(),
    })
