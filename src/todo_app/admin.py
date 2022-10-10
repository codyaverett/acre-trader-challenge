from django.contrib import admin

from .models import Todo, TodoList


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "detail", "created_by", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("title", "detail")


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "todo_count", "created_by", "updated_at")
    list_filter = ("updated_at",)
    search_fields = ("title",)
    list_per_page = 15

    @admin.display(description="Count")
    def todo_count(self, todo_list: TodoList):
        return todo_list.todo.count()
