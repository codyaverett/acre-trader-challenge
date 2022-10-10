from rest_framework import serializers
from datetime import datetime

from ..models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'detail', 'created_at',
                  'completed_at', 'updated_at', 'created_by', 'important')
        lookup_field = 'id'

    # Update a todo's updated_at field when it is updated
    def update(self, instance, validated_data):
        instance.updated_at = datetime.now()
        instance.save()
        return super().update(instance, validated_data)
