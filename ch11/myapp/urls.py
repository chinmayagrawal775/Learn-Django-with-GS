from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.showcontent)
]
