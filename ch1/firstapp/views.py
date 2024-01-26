from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first_app(request):
    return HttpResponse('<h1>Hello Django first app</h1>')