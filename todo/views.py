from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Todo
from .forms import TodoEnterForm

# Create your views here.
def homepage(request):
    if request.method == "POST":
        form = TodoEnterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Task successfully added!')
            #return redirect('homepage')
        else:
            messages.error(request, 'Error saving form')
    else:
        form = TodoEnterForm()
    return render(request, 'todo/homepage.html', {'form': form})

def sign_up(request):
    todo_tasks = Todo.objects.all()

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
    return render(request, 'todo/sign_up.html', {'form': form, 'todo_tasks': todo_tasks})