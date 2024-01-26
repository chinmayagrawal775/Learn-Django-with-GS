from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('delete/<int:id>/', views.Delete.as_view(), name='delete'),
    path('edit/<int:id>/', views.Edit.as_view(), name='edit'),
]
