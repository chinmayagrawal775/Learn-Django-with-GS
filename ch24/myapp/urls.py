from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassView.as_view()),
    path('home/', views.RedirectView.as_view(url='/')),
    path('index/', views.RedirectView.as_view(url='/')),
    # path('', views.TemplateView.as_view(template_name='myapp/classtemp.html')),
]