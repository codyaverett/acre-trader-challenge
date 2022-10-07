from ..models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'detail', 'created_at', 'completed_at', 'updated_at', 'created_by', 'important')