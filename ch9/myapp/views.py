from django.shortcuts import render

# Create your views here.

def home(request, check):
    return render(request, 'myapp/index.html', {'data':check})

def showcontent(request, id, subid=0):
    return render(request, 'myapp/content.html', {'data':[id, subid]})