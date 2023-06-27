from django.shortcuts import render, redirect

# Create your views here.
def first_page(request):
    return render(request, 'todo/base.html')