from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Program,Subprogram,Course
def display(request):
    data=Program.objects.values_list('id','program')
    
    program={}
    subprogram={}
    for idp,p in Program.objects.values_list('id','program'):
        program[p]=[]
        for ids,sp in Subprogram.objects.filter(program_id=idp).values_list('id','subprogram'):
            program[p].append(sp)
            subprogram[sp]=[]
            for c in Course.objects.filter(subprogram_id=ids):
                subprogram[sp].append(c)
 
   

    return render(request,'index.html',{'program':program,'subprogram':subprogram})