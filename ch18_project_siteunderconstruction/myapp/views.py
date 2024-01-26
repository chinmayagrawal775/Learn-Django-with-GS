from django.shortcuts import render

# Create your views here.
def home(request):
    print('home view')
    return render(request, 'myapp/home.html')

def about(request):
    print('about view')
    return render(request, 'myapp/about.html')