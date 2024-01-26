from django.shortcuts import HttpResponse, render

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        print("call from middleware before view")
        # response = HttpResponse("site under construction")
        response = render(request, 'myapp/siteuc.html')
        print("call from middleware after view")
        return response