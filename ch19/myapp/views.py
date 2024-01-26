from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    data = Student.objects.all()
    return render(request, 'myapp/home.html', {'data':data})