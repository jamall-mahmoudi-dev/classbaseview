from django.urls import path
from .views import *


app_name = 'tasks'


urlpatterns = [
path('', TaskListView.as_view(), name='list'),
path('create/', TaskCreateView.as_view(), name='create'),
path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
path('no-permission/', NoPermissionView.as_view(), name='no-permission'),
# path("go-to-aarsaan-co/",RedirectView.as_view(url="http://aarsaan-co.ir/"),name="go-to-aarsaan-co.ir",),
# path('<str:bahram>', test, name='test')
]