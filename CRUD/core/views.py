from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from core.forms import User
from core.models import UserTB
 

# Create your views here.

def addandshow(request):
    try:
        if request.method == 'POST':
            form = User(request.POST)
            if form.is_valid:
                nm = request.POST.get('name')
                em= request.POST.get('email') 
                pas = request.POST.get('password')
                db = UserTB(name=nm,email=em,password=pas)
                db.save()
            return render(request,'add&show.html')    
    except IntegrityError:            
        pass

    form = User() 
    dt = UserTB.objects.all()       
    return render(request, 'add&show.html', {"form":form,"userdata":dt})

def delete(request,stu_id):
    if request:
        d = UserTB.objects.get(pk=stu_id)
        d.delete()
        return HttpResponseRedirect('/')
    
def update(request,stu_id):
    if request.method == 'POST':
        up = UserTB.objects.get(pk=stu_id) 
        fm = User(request.POST,instance=up)
        if fm.is_valid:
            fm.save()
    else:
        if request.method == 'GET':
            up = UserTB.objects.get(pk=stu_id) 
            fm = User(instance=up)
        return render(request,'update.html',{"form":fm})    
             

        