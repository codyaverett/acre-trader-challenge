from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):
    """Test module for Todo model"""

    def test_title(self):
        todo = Todo.objects.create(
            title='Test Todo',
            detail='Test detail',
        )
        self.assertEqual(todo.title, 'Test Todo')
