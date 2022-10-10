from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models import TodoList
from ..serializers import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todo lists to be viewed or edited
    User must be authenticated to access this endpoint
    """

    queryset = TodoList.objects.all().order_by("id")
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title"]
