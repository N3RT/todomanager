from django.http import HttpResponse


def startPage(request):
    return HttpResponse('Start page and Registration/Authentication')

def blog(request):
    return HttpResponse('Blog')

def feedback(request):
    return  HttpResponse('Feedback')