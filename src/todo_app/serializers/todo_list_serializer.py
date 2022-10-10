from rest_framework import serializers
from datetime import datetime

from ..models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'todo', 'updated_at', 'created_by')
        lookup_field = 'id'

    # Update a todoList updated_at field when it is updated
    def update(self, instance, validated_data):
        instance.updated_at = datetime.now()
        instance.save()
        return super().update(instance, validated_data)
