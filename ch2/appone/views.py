from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def app_one(request):
    data = {'page': 'one'}
    return render(request, 'appone/one.html', data)