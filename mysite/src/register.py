import django.http
import django.views.decorators.csrf
import AccountManager

# Progresses into our facility, give us the ability to register for a
# new user to sign up
@django.views.decorators.csrf.csrf_exempt
def register(req):
    if req.method != "POST":
        return django.http.HttpResponseBadRequest("Must use POST")
    uname = req.POST.get("username")
    pwd = req.POST.get("password")
    try:
        AccountManager.addAccount(uname, pwd)
        req.session["user"] = uname
        req.session.modified = True     # Tell Django to update session
        return django.http.HttpResponse("OK")
    except AccountManager.AccountError as e:
        print(e.args)
        return django.http.HttpResponseBadRequest()