def my_middleware_func(get_response):
    print('initial function authentication done......')
    def myfunc(request):
        print('before function view.....')
        reponse = get_response(request)
        print('after function view.....')
        return reponse
    return myfunc

class MyMiddlewareClass:
    def __init__(self, get_response):
        self.get_response = get_response
        print('initial class authentication done...')
    def __call__(self, request):
        print('before class view.....')
        reponse = self.get_response(request)
        print('after class view.....')
        return reponse