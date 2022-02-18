import django.http

def getuser(req):
    # Look in current session for current user
    # Get user field out of it
    u = req.session.get("user", "")
    return django.http.HttpResponse(u)