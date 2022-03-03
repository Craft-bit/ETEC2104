from django.http import HttpResponse

def showHomePage(request):
    return HttpResponse("Hello, world<br><img src='/static/Images/hello_world.png'>")