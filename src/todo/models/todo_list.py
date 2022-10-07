from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from .todo import Todo

class TodoList(models.Model):
    """
    List model
    """
    title = models.CharField(max_length=100)
    todo = models.ManyToManyField(Todo, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # def create_list(self, title, user):
    #     self.title = title
    #     self.created_by = user
    #     self.save()
    
    class Meta:
        ordering = ['title']

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'todo', 'updated_at', 'created_by')