from django.urls import path
from .views import *


app_name = 'tasks'


urlpatterns = [
path('', TaskListView.as_view(), name='list'),
path('create/', TaskCreateView.as_view(), name='create'),
path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
# path("go-to-maktabkhooneh/",RedirectView.as_view(url="https://maktabkhooneh.org/"),name="go-to-maktabkhooneh",),
# path('<str:bahram>', test, name='test')
]