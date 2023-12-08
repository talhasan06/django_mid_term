from django.shortcuts import render,redirect
from . import forms
from .models import Task
# Create your views here.
def show_tasks(request):
    data=Task.objects.all()
    return render (request,'show_tasks.html',{'data':data})

def add_task(request):
    if request.method =='POST':
        task_form=forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = forms.TaskForm()

    return render(request,'add_task.html',{'form':task_form})

def edit_task(request,id):
    task=Task.objects.get(pk=id)
    task_form=forms.TaskForm(instance=task)

    if request.method =='POST':
        task_form=forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')

    return render(request,'add_task.html',{'form':task_form})

def delete_task(request,id):
    task=Task.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')
