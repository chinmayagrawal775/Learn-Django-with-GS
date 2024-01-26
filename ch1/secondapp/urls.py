from django.urls import path
from . import views

urlpatterns = [
        path('secondapp/', views.second_app),
]