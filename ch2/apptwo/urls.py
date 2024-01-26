from django.urls import path
from . import views

urlpatterns = [
    path('apptwo/', views.app_two),
]