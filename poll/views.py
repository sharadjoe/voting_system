from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Team, Backer
def index(request):
    teams = Team.objects.all()
    counter = 0 
    data = []
    for i in teams:
        val = 0
        if counter == 3:
            print("Hello")
            counter = 0
            val = 1
        data.append({  "url":"/vote?id="+str(i.id), "Name" : i.Name , "Image" : i.Image , "Bot" : i.Bot , "Members" : i.Members , "Val" : val}  ) 
        counter += 1

    context = {'teams':data} 
    return render(request,'index.html',context)

def vote(request):
    if("id" not in request.GET.keys()):return HttpResponseRedirect("/")
    team = Team.objects.all().filter(id=request.GET.get("id",0))
    backers = Team.objects.get(id=request.GET.get("id",0)).Backers.all()
    return render(request,'hero.html',{'teams':team , "url" : "/confirm?id=" + str(request.GET.get("id",0)) ,"backer" : backers })
