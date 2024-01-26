from django.shortcuts import render
from .forms import StudentForm
from .models import UserModel

# Create your views here.
def showform(request):
    if request.method == 'POST':
        f = StudentForm(request.POST)
        if f.is_valid():
            print(f.cleaned_data['name'])
            print(f.cleaned_data['email'])
            reg = UserModel( name=f.cleaned_data['name'], email=f.cleaned_data['email'])
            # reg = UserModel(id=1, name=f.cleaned_data['name'], email=f.cleaned_data['email'])
            reg.save()
            # reg = UserModel(id=1)
            # reg.delete()
    else:
        f = StudentForm()
    return render(request, 'myapp/content.html', {'form':f})