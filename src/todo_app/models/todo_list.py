from django.db import models
from django.contrib.auth.models import User

from .todo import Todo


class TodoList(models.Model):
    """
    A todolist represents a collection of todos.
    """
    title = models.CharField(max_length=100)
    todo = models.ManyToManyField(Todo, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
