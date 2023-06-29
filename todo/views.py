from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404

from .models import Task, Subtask
from .forms import TodoEnterForm, CreateSubtaskForm


# Create your views here.
def homepage(request):
    todo_tasks = Task.objects.all()
    subtasks = {t.pk: t.subtask_set.all() for t in todo_tasks}
    if request.method == "POST":
        form = TodoEnterForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            messages.success(request, 'Your Task successfully added!')
            return redirect('homepage')
        else:
            messages.error(request, 'Error saving form')
    else:
        form = TodoEnterForm()
    return render(request, 'todo/homepage.html', {'form': form, 'todo_tasks': todo_tasks, 'subtasks': subtasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    subtask_list = task.subtask_set.all()
    print(subtask_list)
    if request.method == "POST":
        form = CreateSubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('task_detail', pk=pk)
        else:
            messages.error(request, 'Error saving form')
    else:
        form = CreateSubtaskForm()
    return render(request, 'todo/task_detail.html', {'task': task, 'form': form, 'subtask_list': subtask_list})


def done_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done_task()
    task.save()
    return redirect('homepage')


def cancel_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.cancel_task()
    task.save()
    return redirect('homepage')


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'todo/sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('homepage')
            else:
                messages.error(request, f"Invalid username or password.")
        else:
            messages.error(request, f"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'todo/log_in.html', {'form': form})


def log_out(request):
    logout(request)
    messages.info(request, f"You successfully is logout.")
    return redirect('homepage')
