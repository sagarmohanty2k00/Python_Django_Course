from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Task
from django.http import HttpResponseRedirect

def home(request):
    todo_items = Task.objects.all().order_by("-added_date")
    data = {
        "tasks": todo_items
    }
    return render(request, 'todo.html', data)

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    Task.objects.create(added_date=current_date, taskName=content)

    return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
    Task.objects.get(id=todo_id).delete()

    return HttpResponseRedirect('/')