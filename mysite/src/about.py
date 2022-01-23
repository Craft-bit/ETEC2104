"""
Importing a django shortcut
Import time to have some dynamic content (time of day or something)
Create a function called view (views the time)
* Return calls django's templating system
    * Gets the request from the client
    * Gets the dictionary created
"""

from django.shortcuts import render
import time

def view(req):
    ctx = {
        "name" : "Bob",
        "now" : time.asctime()
    }
    return render( req, "about.html", ctx )