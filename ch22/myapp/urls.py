from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.funview),
    path('', views.ClassView.as_view()),
]