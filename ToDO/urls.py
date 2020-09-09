from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "todo"
urlpatterns = [
    path('',views.tasks , name='todo' ),
    path('update/<int:pk>/', views.update, name='update'),
    path('create/', views.create_task , name='create'),
    path('delete/<int:pk>/', views.task_delete, name='delete'),
]
