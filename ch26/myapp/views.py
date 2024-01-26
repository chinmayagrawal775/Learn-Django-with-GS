from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Student
from . forms import AddForm

# Create your views here.

# class Home(ListView):
#     model = Student

# class Home(DetailView):
#     model = Student

# class Home(FormView):
#     template_name = 'myapp/addform.html'
#     form_class = AddForm
#     def form_valid(self, form):
#         print(form)
#         print(form.cleaned_data['name'])
#         return HttpResponseRedirect('/')

# class Home(CreateView):
#     model = Student
#     fields = ['name']
#     success_url = '/'

# class Home(UpdateView):
#     model = Student
#     fields = ['name']
#     success_url = '/'

class Home(DeleteView):
    model = Student
    success_url = '/'