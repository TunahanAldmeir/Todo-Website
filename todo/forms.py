from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Toodo


class TodoForm(forms.ModelForm):
    class Meta:
        model=Toodo
        fields='__all__'



