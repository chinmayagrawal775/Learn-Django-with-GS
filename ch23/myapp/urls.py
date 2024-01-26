from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassView.as_view()),
    # path('', views.TemplateView.as_view(template_name='myapp/classtemp.html')),
]