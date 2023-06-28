from django import forms
from .models import Todo

class TodoEnterForm(forms.ModelForm):
    #title = forms.CharField(max_length=200, required=True, help_text='Enter a base description of your task.')
    #todo_desc = forms.CharField(max_length=1000, help_text='Enter an extended description of your task.')

    class Meta:
        model = Todo
        fields = ('title', 'text')