from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import UserModel
from django.views.generic.base import View, TemplateView, RedirectView

# Create your views here.
class Index(TemplateView):
    template_name = 'user/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserForm()
        data = UserModel.objects.all()
        display_data = {
            'form': form,
            'data': data
        }
        return display_data
        
    def post(self, request):
        form = UserForm(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            reg = UserModel(name=name, email=email, age=age)
            reg.save()
            return HttpResponseRedirect('/')

class Delete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        pi = UserModel.objects.get(pk=kwargs['id'])
        pi.delete()
        return super().get_redirect_url(*args, **kwargs)

class Edit(View):
    def get(self, request, id):
        pi = UserModel.objects.get(pk=id)
        form = UserForm(instance=pi)
        return render(request, 'user/edituser.html', {'form':form})

    def post(self, request, id):
        pi = UserModel.objects.get(pk=id)
        form = UserForm(request.POST, instance=pi)
        if(form.is_valid()):
            form.save()
        return HttpResponseRedirect('/')