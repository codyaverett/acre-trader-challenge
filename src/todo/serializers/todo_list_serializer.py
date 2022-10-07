from ..models import Todo, TodoList
from rest_framework import serializers


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'todo', 'updated_at', 'created_by')
        lookup_field = 'id'
