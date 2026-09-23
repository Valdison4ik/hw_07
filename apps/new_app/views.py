from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new_view(request):
    return HttpResponse("<h1>Hello Vlada!</h1>\n<h2>This is your homework assignment number 7.</h2>")