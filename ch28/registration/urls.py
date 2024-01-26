from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', views.Profile.as_view()),
    # path('profile/', login_required(views.Profile.as_view())),
]