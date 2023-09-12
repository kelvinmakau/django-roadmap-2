from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView #List view
from django.views.generic.detail import DetailView #Detail View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Task #import our models


# Create your views here.

#function based view
def home(request):
    return render(request, 'home.html')

# Class based views
# List View - Lists objects - List tasks,
class TaskList(ListView): 
    model = Task
    context_object_name = 'tasks'

# Detail View - displays the details of an object
class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"

# View for creating tasks
class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(TaskCreate,self).form_valid(form)
    
# View for updating the Todo tasks
class TaskUpdate(UpdateView):
    model=Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "The task has been updated successfully")
        return super(TaskUpdate,self).form_valid(form)

# Delete view
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)
