# Utilities just for testing
import django.test

def createAccount(username, password):
    c = django.test.Client()
    resp = c.post("/register", {"username":username,"password":password})
    return resp

def createAccountNoPassword(username):
    c = django.test.Client()
    resp = c.post("/register", {"username":username})
    return resp

def createAccountNoUsername(password):
    c = django.test.Client()
    resp = c.post("/register", {"password":password})
    return resp