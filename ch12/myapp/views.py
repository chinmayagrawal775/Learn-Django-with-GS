from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'geek'
    return render(request, 'myapp/setsession.html')

def getsession(request):
    name = request.session['name']
    return render(request, 'myapp/getsession.html', {'name': name})

def delsession(request):
    del request.session['name']
    return render(request, 'myapp/delsession.html')