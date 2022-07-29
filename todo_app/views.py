from multiprocessing import context
from django.shortcuts import render,HttpResponse
from .models import Todo
# Create your views here.

def index(request):
    return render(request,'index.html')


def view_todo(request):
    todos = Todo.objects.all()
    context = {
        "todos":todos
    }
    return render(request,'view_todo.html',context)


def add_todo(request,):
    if request.method =='POST':
        title = request.POST['title']
        todo = request.POST['todo']
        new_todo = Todo(title=title,todo=todo)
        new_todo.save()
        return HttpResponse("todo is added check it out!")

    elif request.method =='GET':
        return render(request,'add_todo.html')

    else:
        return HttpResponse("something is wrong")



def del_todo(request,tod_id=0):
    if tod_id:
        try:
            todo_to_be_deleted = Todo.objects.get(id=tod_id)
            todo_to_be_deleted.delete()
            return HttpResponse("deleted successfully")
        except:
            return HttpResponse("not found")

    todos = Todo.objects.all()
    context = {
        "todos":todos
    }
    return render(request,'del_todo.html',context)