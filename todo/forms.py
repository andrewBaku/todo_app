from django import forms
from django.forms import Textarea

from .models import Task

class TodoEnterForm(forms.ModelForm):
    #title = forms.CharField(max_length=200, required=True, help_text='Enter a base description of your task.')
    #todo_desc = forms.CharField(max_length=1000, help_text='Enter an extended description of your task.')
    class Meta:
        model = Task
        fields = ('title', 'text')
        widgets = {
            'text': Textarea(attrs={'cols': 20, 'rows': 5}),
        }