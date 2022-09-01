
from django.contrib import messages
from django.shortcuts import render,redirect

from todo.forms import TodoForm
from .models import Toodo

# Create your views here.

def index(request):
    item_list=Toodo.objects.order_by("-date")

    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form=TodoForm()        

    page={
        "todo_list":item_list,
        "forms":form,
    }

    return render(request,"todo/index.html",page)


def remove(request,item_id):
    item=Toodo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"The task is removed and complete! You should rest 5 minute")
    return redirect('todo')