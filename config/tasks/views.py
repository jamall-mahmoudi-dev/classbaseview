# from os import name
from django.shortcuts import render
from tasks.models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin  # PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
# from .models import Task
from .forms import TaskForm



class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)








def test(request, bahram):
    user = request.user  # current user 
    print(user)  # only for test dev
   # context = {'bahram': bahram}
    context = {
    'users': request.user,
    'tasks': Task.objects.filter(user=request.user)
}
    return render(request, 'tasks/test.html', context)  
