from django.http import HttpResponse


def User(request):
    return HttpResponse("Hello User")


def dummy(request):
    return HttpResponse('Dummy')
