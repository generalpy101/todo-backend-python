from django.urls import path

from .views import (
    GetAllTodos,
    GetCreateTodos,
    GetAllTags,
    GetUpdateDeleteTodo,
)

urlpatterns = [
    path("todos",view=GetCreateTodos.as_view(),name="get_create_todos"),
    path("todos/<pk>",view=GetUpdateDeleteTodo.as_view(),name="get_update_delete_todo"),
    path("tags",view=GetAllTags.as_view(),name="all_tags"),
]