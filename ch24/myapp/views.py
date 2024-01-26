from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class ClassView(TemplateView):
    template_name = 'myapp/classtemp.html'