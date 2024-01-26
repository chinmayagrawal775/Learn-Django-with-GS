from django.shortcuts import render, HttpResponse

# Create your views here.
def setsession(request):
    request.session['name'] = 'geek'
    return render(request, 'myapp/setsession.html')

def getsession(request):
    if('name' in request.session):
        name = request.session['name']
        request.session.modified = True
        return render(request, 'myapp/getsession.html', {'name': name})
    else:
        return HttpResponse('your session has been expired')

def delsession(request):
    del request.session['name']
    return render(request, 'myapp/delsession.html')