from django.core import validators
from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name', 'email']
        labels = {'name':'your name'}
        error_messages = {'name':{'required':'ye jarori hai'}}