from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def app_two(request):
    data = {'page': 'two'}
    return render(request, 'apptwo/two.html', context=data)