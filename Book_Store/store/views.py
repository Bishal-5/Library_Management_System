from django.shortcuts import render
from django.http import HttpResponse
from store.models import *

# Create your views here

def home(request):
    books = Book.objects.all()
    context = {
        'name': 'SVIST',
        'location': 'Baruipur',
        'book': books
    }
    return render(request, "index.html", context)

def addbook(request):
    return render(request, "addbook.html")

def about(request):
    context = {
        'name': 'Bishal Naskar',
        'location': 'Kolkata',
        'email': 'abc@gmail.com',
        'phone': 1234567891
    }
    return render(request, "about.html", context)

def contact(request):
    return render(request, "contact.html")

def parameter(request, number):
    return HttpResponse(number) 