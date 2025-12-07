from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def addTask(request):
    addTask=request.POST['task']
    Todo.objects.create(task=addTask)
    return redirect("home")

def markAsDone(request,pk):
    markDone=get_object_or_404(Todo,pk=pk)
    markDone.is_completed=True
    markDone.save()
    return redirect("home")

def markAsUndo(request,pk):
    markUndo=get_object_or_404(Todo,pk=pk)
    markUndo.is_completed=False
    markUndo.save()
    return redirect("home")