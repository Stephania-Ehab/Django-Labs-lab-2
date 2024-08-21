from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from track.models import *

# Create your views here.

def trainee_list(request):
    # trainee=[]
    # trainee1={'id':1,'name':'stephania ehab','email':'stephania@gmail.com','age':23,'address':'El-Fayoum','trackID':1}
    # trainee2={'id':2,'name':'veronia ehab','email':'veronia@gmail.com','age':20,'address':'El-Fayoum','trackID':2}
    # trainee.append(trainee1)
    # trainee.append(trainee2)
    # context={}
    # context['trainees']=trainee
    # return render(request,'trainee/list.html',context)
    context={}
    trainees=Trainee.objects.all()
    context['trainees']=trainees
    return render(request,'trainee/list.html',context)


def trainee_update(request, id):
    # # context = {}
    # context = {"id": id}
    # return render(request, "trainee/update.html", context)
    context={'trainee':Trainee.objects.get(pk=id)}
    return render(request,'trainee/details.html',context)

def trainee_delete(request, id):
    # context = {}
    context = {"id": id}
    return render(request, "trainee/delete.html", context)

def trainee_details(request, id):
    # context = {}
    context = {"id": id}
    return render(request, "trainee/details.html", context)

def trainee_create(request):
    context={}
    context['tracks']=Track.objects.all()
    if(request.method=='POST'):
        context={}
        if(len(request.POST['traineename'])>0 and len(request.POST['traineename'])<=100):
            traineeobj=Trainee()
            traineeobj.name=request.POST['traineename']
            traineeobj.email=request.POST['traineeemail']
            traineeobj.age=request.POST['traineeage']
            traineeobj.phone=request.POST['traineephone']
            traineeobj.trackobj=Track.objects.get(pk=request.POST['traineetrackid'])
            traineeobj.save()
        else:
            context['error']='invalid'

    return render(request, "trainee/create.html")
