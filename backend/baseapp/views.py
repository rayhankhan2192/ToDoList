from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'baseapp/task.html'
    
class TaskCreate(CreateView):
    model = Task
    #fields = '__all__'
    fields = [
        'user',
        'title',
        'description',
        'complete',
    ]
    success_url = reverse_lazy('tasks')
    
class TakeUpdate(UpdateView):
    model = Task
    fields = [
        'user',
        'title',
        'description',
        'complete',
    ]
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks') 
    