# from os import name
from django.shortcuts import render
from tasks.models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin  # PermissionDenied
from django.urls import reverse_lazy
# from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView




class TaskListView(LoginRequiredMixin, ListView):
    # queryset = Task.objects.all()
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 3 

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    #fields = []
    success_url = reverse_lazy('tasks:list')   

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'تسک "{form.instance.title}" با موفقیت ایجاد شد!')

        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'تسک "{form.instance.title}" با موفقیت ویرایش شد!')
        return response

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')
    # success_url = '/'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        task = self.get_object()  
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'تسک "{task.title}" با موفقیت حذف شد!')
        return response

class NoPermissionView(TemplateView):
    template_name = 'no_permission.html'




def test(request, bahram):
    user = request.user  # current user 
    print(user)  # only for test dev
   # context = {'bahram': bahram}
    context = {
    'users': request.user,
    'tasks': Task.objects.filter(user=request.user)
}
    return render(request, 'tasks/test.html', context)  
