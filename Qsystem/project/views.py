# coding=utf-8
from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from project.models import *
from django.db import connection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from forms import changedesignForm,delayprojectForm
import datetime
from django.contrib.auth import *
#from django.template import RequestContext


# Create your views here.

def personal_homepage(request):
    result=project.objects.exclude(Q(status_p=u'已上线')| Q(status_p=u'暂停'))
    result1=project.objects.exclude(~Q(status_p=u'已上线')& ~Q(status_p=u'暂停'))
    puser=project_user.objects.all()
    return render_to_response('personal_homepage.html',
        {'result':result,'result1':result1,'puser':puser})

def deleteproject(request,id):
    delpro=get_object_or_404(project,pk=int(id))    
    delpro.delete()
    return HttpResponseRedirect(reverse("homepage"))


def pauseproject(request,id):
    pausepro=get_object_or_404(project,pk=int(id))
    pausepro.status_p='暂停'
    pausepro.save()
    return HttpResponseRedirect(reverse("homepage"))

def delayproject(request):
    if request.method=='POST':
        form = delayprojectForm(request.POST)
        if form.is_valid():
            delayid=form.cleaned_data['delayid']
            delay_date = form.cleaned_data['delay_date']
            delay_reason = form.cleaned_data['delay_reason']
            delpro=project.objects.get(id=delayid)
            uid=delpro.leader_p
            protitle=delpro.project
            delay_p=project_delay(application=uid,project_id=delayid,delay_to_date=delay_date,apply_date=datetime.datetime.now(),title=protitle,reason=delay_reason,result="jieshou",review_date=datetime.datetime.now(),isactived="1")
            delay_p.save()                   
    return HttpResponseRedirect(reverse("homepage"))


def changedesign(request):    
          
    if request.method=='POST':
        form = changedesignForm(request.POST)
        if form.is_valid():
            changeid=form.cleaned_data['changeid']
            content = form.cleaned_data['content']
            dpath = form.cleaned_data['dpath']
            chd=project.objects.get(id=changeid)
            uid=chd.leader_p
            chd.blueprint_p=dpath
            chd.save()
            pub_message=public_message(project_id=changeid,publisher=uid,content=content,type_p="message",publication_date=datetime.datetime.now(),isactived="1")
            pub_message.save()           
    return HttpResponseRedirect(reverse("homepage"))