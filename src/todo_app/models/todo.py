from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """
    A todo represents a single task that needs to be completed.
    """
    title = models.CharField(max_length=100)
    detail = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=False, default=1)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['updated_at']
