from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    print('this is view')
    return HttpResponse('this is home page')