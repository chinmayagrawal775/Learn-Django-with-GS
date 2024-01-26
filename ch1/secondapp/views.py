from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second_app(request):
    return HttpResponse('<h1>Hello Django second app</h1>')