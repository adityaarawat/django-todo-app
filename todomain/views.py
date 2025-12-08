from django.shortcuts import render
from todos.models import Todo
from datetime import date

def home(request):
    today = date.today()
    task=Todo.objects.filter(is_completed=False)
    completedTask=Todo.objects.filter(is_completed=True)
    context={
        "tasks":task,
        "completedTask":completedTask,
        "today":today,
    }
    return render(request,'index.html',context)