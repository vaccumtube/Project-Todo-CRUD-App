
from django import forms
from django.forms import ModelForm

from .models import TodoApp
    
class TodoForm(forms.ModelForm):
    input=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"write here"}))
    class Meta:
        model=TodoApp
        fields="__all__"



    


    
