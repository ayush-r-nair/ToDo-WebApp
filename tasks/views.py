from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url='/users/login')
def tasks_view(request):
    tasks=Task.objects.filter(author=request.user,done=False).order_by('date')
    return render(request,'tasks/tasks_view.html',{'tasks':tasks})

def task_page(request,slug):
    task=Task.objects.get(slug=slug)
    return render(request,'tasks/task_page.html',{'task':task})

@login_required(login_url='/users/login')
def task_add(request):
    if request.method=='POST':
        form=forms.CreateTask(request.POST,request.FILES)
        if form.is_valid():
            newtask=form.save(commit=False)
            newtask.author=request.user
            newtask.save()
            return redirect('tasks:view')
    else :
        form =forms.CreateTask()
    return render(request,'tasks/task_add.html',{'form':form})

def task_update(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        form = forms.CreateTask(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:view')
    else :
        form =forms.CreateTask(instance=task)
    return render(request,'tasks/task_update.html',{'form':form, 'task':task})

def task_delete(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('tasks:view')
    return render(request,'tasks/task_delete.html',{'task':task})

def task_complete(request,pk):
    task=Task.objects.get(id=pk)
    task.done=True
    task.save()
    return redirect('tasks:view')
    