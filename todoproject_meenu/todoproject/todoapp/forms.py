from . models import Task
from django import forms
class TodoForm(forms.ModelForm):
    class meta:
        model=Task
        fields=['name','priority','date']
