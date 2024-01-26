from django.shortcuts import render
from . import forms
# Create your views here.
def showform(request):
    f = forms.StudentForm()
    return render(request, 'myapp/content.html', {'form': f})