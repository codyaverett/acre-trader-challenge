from ..models import TodoList
from ..serializers import TodoListSerializer
from rest_framework import viewsets
from rest_framework import permissions


class TodoListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todo lists to be viewed or edited
    User must be authenticated to access this endpoint 
    """
    queryset = TodoList.objects.all().order_by('id')
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
