from django.shortcuts import render
from todos.models import Todo

def home(request):
    task=Todo.objects.filter(is_completed=False)
    completedTask=Todo.objects.filter(is_completed=True)
    context={
        "tasks":task,
        "completedTask":completedTask
    }
    return render(request,'index.html',context)