from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'page/index.html')

def contact(request):
    return render(request, 'page/contact.html')