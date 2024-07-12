from django.shortcuts import render
from .models import project2

# Create your views here.
def home(request):
    return render(request,'index.html')

def courseshow(request):
    return render(request,'course.html ')

def result(request):
    return render(request, 'result.html')

def contact(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    qualification=request.POST.get('qualification')
    r2=project2(name=name, email=email, qualification=qualification)
    r2.save()
    return render(request, 'contact.html')




def about(request):
    return render(request, 'aboutvi.html')


def register(request):
    return render(request, 'registration.html')





def automation(request):
    return render(request, 'Automation.html')


def autocad(request):
    return render(request, 'autocad.html')


def dm(request):
    return render(request, 'DM.html')


def ds(request):
    return render(request, 'DS_AI.html')


def embedded(request):
    return render(request, 'embedded.html')


def java(request):
    return render(request, 'javaFS.html')


def plc(request):
    return render(request, 'PLC.html')


def python(request):
    return render(request, 'python.html')