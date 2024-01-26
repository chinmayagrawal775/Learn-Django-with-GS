from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import MyForm

# Create your views here.
def funview(request):
    return HttpResponse('<H1> function based view<H1>')

class ClassView(View):
    def get(self, request):
        form = MyForm()
        context = {'msg': form}
        # return HttpResponse('<H1> class based view - get<H1>')
        return render(request, 'myapp/classtemp.html', context)
    
    def post(self, request):
        form = MyForm(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
        return HttpResponse('<H1>Form submitted... <H1>')