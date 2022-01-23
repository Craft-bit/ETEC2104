from django.http import HttpResponse

def showHomePage(request):
    return HttpResponse("Hello, world<br><img src='/static/hello_world.png'>")