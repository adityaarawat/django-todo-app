from django.shortcuts import redirect,get_object_or_404,render
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

def editTodo(request,pk):
    editData=get_object_or_404(Todo,pk=pk)
    if request.method=="POST":
        updated_task=request.POST['task']
        editData.task=updated_task
        editData.save()
        return redirect("home")
    else:
        context={
        "editData":editData
        }
        return render(request,'editTodo.html',context)  
    
def deleteTodo(request,pk):
    deleteTodo=get_object_or_404(Todo,pk=pk)
    deleteTodo.delete()
    return redirect("home")