from django.urls import path
from . import views
urlpatterns=[
    #Add Task
    path('addTask/',views.addTask,name='addTask'),

    #Mark As Done
    path('mark_as_done/<int:pk>/',views.markAsDone,name="markAsDone"),

    #Mark As Undo
    path("mark_as_undo/<int:pk>/",views.markAsUndo,name='markAsUndo'),

    #Edit 
    path("edit_todo/<int:pk>/",views.editTodo,name='editTodo'),

    #delete
    path("delete_todo/<int:pk>/",views.deleteTodo,name="deleteTodo")
]