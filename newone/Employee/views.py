from django.shortcuts import render
from .models import Employee
# Create your views here.o

def home_view(request,*args,**kwargs):
    obj = Employee.objects.all()
    context = {
        'obj1': obj
    }
    return render(request,"home.html",context)

def index_view(request):

    return render(request,"index.html",{})

