from ..models import Todo
from ..serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework import permissions


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited
    User must be authenticated to access this endpoint 
    """
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
