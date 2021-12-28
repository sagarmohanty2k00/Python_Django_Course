from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add-todo/', views.add_todo),
    path('delete-todo/<int:todo_id>/', views.delete_todo),
]