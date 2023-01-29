from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')
    return render(request,'topic.html')


def webpage(request):
    td=Topic.objects.all()
    d={'td':td}
    if request.method=="POST":
        tn=request.POST['tn']
        w=request.POST['usn']
        u=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=w,url=u)[0]
        W.save()
        return HttpResponse('webpage insert done')
    return render(request,'webpage.html',d)

def access(request):
    rd=Webpage.objects.all()
    d={'rd':rd}
    if request.method=='POST':
        Q=request.POST['tn']
        N=request.POST['usn']
        u=request.POST['url']
        D=request.POST['date']
        E=Topic.objects.get_or_create(topic_name=Q)[0]
        E.save()
        R=Webpage.objects.get_or_create(topic_name=E,name=N,url=u)[0]
        R.save()
        A=AccessRecords.objects.get_or_create(name=R,date=D)[0]
        A.save()
        return HttpResponse('Access is done')
    return render(request,'access.html',d)