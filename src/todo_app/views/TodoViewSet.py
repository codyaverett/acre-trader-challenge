from rest_framework import viewsets, permissions

from ..serializers import TodoSerializer
from ..models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited
    User must be authenticated to access this endpoint 
    """
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
