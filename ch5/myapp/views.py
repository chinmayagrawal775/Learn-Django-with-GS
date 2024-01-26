from django.shortcuts import render
from .models import Student
# Create your views here.
def showdata(request):
    df = Student.objects.all()
    return render(request, 'myapp/content.html', {'data':df})