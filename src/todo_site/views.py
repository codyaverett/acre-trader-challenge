from django.shortcuts import render
from todo_app.models import Todo, TodoList


def site(request):
    return render(request, 'site.html', {
        'todos': Todo.objects.all(),
        'todo_lists': TodoList.objects.all(),
    })
