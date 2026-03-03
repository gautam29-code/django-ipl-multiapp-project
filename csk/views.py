from django.shortcuts import render
from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1>ms dhoni is the captain of csk</h1>")
def vicecaptain(request):
    return HttpResponse("<h1>suresh raina is the vicecaptain of csk</h1>")
