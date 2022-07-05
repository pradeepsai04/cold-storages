from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    

    return render(request,'.\home1.html')
def add(request):
    x=float(request.POST["num1"])
    y=float(request.POST["num2"])
    res=x+y
    return render(request,"result.html",{'result':res})    