def Middlewareoperation(get_response):
    def middleware(request):
        print("This will run before the view")
        response=get_response(request)
        print("This will run after the view")
        return response
    return middleware


def Standardmiddleoperation(get_response):
    def middleware(request):
        print("This is Standardmiddleoperation  and this will run before the view")
        response=get_response(request)
        print("This is Standardmiddleoperation  and this will run after the view")
        return response
    return middleware



def CustomMiddleware(get_response):
    def middleware(request):
        print("This is CustomMiddleware and this will run before the view")
        response=get_response(request)
        print("This is CustomMiddleware and this will run after the view")
        return response
    return middleware


def UserMiddleware(get_response):
    def middleware(request):
        print("This is UserMiddleware and this will run before the view")
        response=get_response(request)
        print("This is UserMiddleware and this will run after the view")
        return response
    return middleware
