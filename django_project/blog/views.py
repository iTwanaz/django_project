from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(request, 'blog/home.html')

def about(request):
    return HttpResponse('<h1>Hello About!</h1>')