from django.shortcuts import redirect
from django.urls import resolve

class TaskAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        task_id = view_kwargs.get('pk')

        # اگر لاگین نیست → بفرست به صفحه لاگین
        if task_id and not request.user.is_authenticated:
            return redirect('login')

        if task_id and request.user.is_authenticated:
            from .models import Task
            try:
                task = Task.objects.get(pk=task_id)
            except Task.DoesNotExist:
                return redirect('no-permission')

            if task.user != request.user:
                return redirect('no-permission')

        return None
