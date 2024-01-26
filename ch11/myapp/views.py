from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def showcontent(request):
    if(request.method == 'POST'):
        # messages.add_message(request, messages.SUCCESS, 'message showing')
        messages.success(request, 'account created')
        print(messages.get_level(request))
        messages.set_level(request, messages.DEBUG)
        messages.debug(request, 'account created')
        print(messages.get_level(request))
    return render(request, 'myapp/content.html')