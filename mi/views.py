from django.shortcuts import render
from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1>rohit is the captain of mi</h1>")
def vicecaptain(request):
    return HttpResponse("<h1>surya is the vicecaptain of mi</h1>")
