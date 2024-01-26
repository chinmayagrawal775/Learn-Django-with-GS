from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# def profile(request):
#     return render(request, 'registration/profile.html')

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = 'registration/profile.html'
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)