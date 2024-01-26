from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
class ClassView(TemplateView):
    template_name = 'myapp/classtemp.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'geek'
        return context