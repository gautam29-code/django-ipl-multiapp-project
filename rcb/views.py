from django.shortcuts import render
from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1>virat is the captain of csk</h1>")
def vicecaptain(request):
    return HttpResponse("<h1>patidar is the vicecaptain of csk</h1>")
