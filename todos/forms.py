from django import forms
from . models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model=Task
        fields=("title",)
        widgets={"title":forms.TextInput(attrs={"type":"text","class":"form-control","id":"title","placeholder":"please add your wish"})}