from django.http import HttpRequest
from django.views import View

# from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpRequest('Hello World from function!')


class HelloView(View):
    def get(self, request):
        return HttpRequest('Hello World from class!')
