import http

from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import todo_model
# Create your views here.

def index(request):
    todos = todo_model.objects.all()
    return render(request, 'todolist/index.html', {'todo_list': todos, 'title': 'Главная страница'})

@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    todo = todo_model(title=title)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = todo_model.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = todo_model.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
