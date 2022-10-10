from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from .todo import Todo


class TodoList(models.Model):
    """
    A todolist represents a collection of todos.
    """
    title = models.CharField(max_length=100)
    todo = models.ManyToManyField(Todo, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
