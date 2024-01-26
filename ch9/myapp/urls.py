from django.urls import path, register_converter
from . import converters, views

register_converter(converters.Converter, 'convert')

urlpatterns = [
    path('', views.home, {'check':'OK'}, name='home'),
    path('myapp/<int:id>/<subid>', views.showcontent, name='content'),
    path('convert/<convert:id>', views.showcontent, name='content'),
]
