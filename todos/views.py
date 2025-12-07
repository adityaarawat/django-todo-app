from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def addTask(request):
    addTask=request.POST['task']
    Todo.objects.create(task=addTask)
    return redirect("home")