from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import *

# Create your views here.
def home(request):
    student = Student.objects.all()
    context = {
        'name': 'SVIST',
        'location': 'Baruipur',
        'students': student
    }
    return render(request, "index.html", context)

def manage(request):
    return render(request, "manage.html")