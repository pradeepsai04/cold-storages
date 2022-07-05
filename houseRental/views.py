from django.shortcuts import render,redirect
from .models import dest,house
from django.contrib.auth.models import User
def page1(request):
    dests=dest.objects.all()
    return render(request,'page.html',{'d':dests})
def next(request):
    houses=house.objects.all()
    return render(request,'page2.html',{'h':houses})    
def register(request):
    if request.method=='POST':
        
        first=request.POST['firstname']
        last=request.POST['lastname']
        user=request.POST['username']
        password1=request.POST['password1']
        
        location=request.POST['location']
        email=request.POST['email']
        user  = User.objects.create_user(username=user,first_name=first,last_name=last,password=password1,email=email)
        user.save();  
        print("user created")
        
        return redirect('home')
    else:    
        return render(request,'result.html')
def nextonline(request):
    return render(request,'page3.html')        

# Create your views here.
