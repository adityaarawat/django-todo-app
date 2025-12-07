from django.shortcuts import render
from todos.models import Todo

def home(request):
    task=Todo.objects.filter(is_completed=False)
    context={
        "tasks":task
    }
    return render(request,'index.html',context)