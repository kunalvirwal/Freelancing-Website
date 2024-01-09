from django.shortcuts import render,redirect
from producer.models import *

# Create your views here.
def freelancer_info(request,obj):
    l=[]
    job=jobs.objects.all()
    user_email=obj.email
    for i in job:
        a=i.applied_emails.split(",")
        if user_email in a:
            j=recruiters.objects.get(email=i.rec)
            l.append([i,j])
            
    params={  
        "name":obj.name,
        "about":obj.about,
        "profile_pic":obj.profile_pic,
        "email":obj.email,
        "phone":obj.phone,
        "role":obj.role,
        "profession":obj.profession,
        "org":obj.org,
        "address":obj.address,
        "jobs":l
    }
    response=render(request,"freelancer_profile.html",params)
    response.set_cookie('user_email', obj.email)  
    response.set_cookie('user_role', obj.role)
    return response

def job_list(request):
    job=jobs.objects.all()
    user_email= request.COOKIES["user_email"]
    l=[]
    for i in job:
        a=i.applied_emails.split()
        if user_email not in a:
            
            j=recruiters.objects.get(email=i.rec)
            
            l.append([i,j])
            
    return render(request,"joblist.html",{"jobs":l,})


def jobviewpage(request,id):
    job=jobs.objects.get(id=id)
    s=recruiters.objects.get(email=job.rec)
    fromhome=False
    user_email= request.COOKIES["user_email"]
    a=job.applied_emails.split(",")
    if user_email in a:
         fromhome=True
        
        
    params={
        "id":id,
        "guy":job.name,
        "quant":job.quantity,
        "prc":job.pay,
        "hrs":job.time,
        "desc":job.desc,
        "opener":s.name,
        "fromhome":fromhome,
        "sid":s.id,
        "pic":s.profile_pic,
        "email":s.email,
        "phn":s.phone,
        
    }
    
    return render(request,"jobviewpage.html",params)

def addinterest(request,id):
    
    job=jobs.objects.get(id=id)
    user_email=request.COOKIES["user_email"]
    s=job.applied_emails
    a=s.split(",")
    
    if user_email in a:
        pass
    else:
        if s=="":
            s=user_email
        else:
            s+=(","+user_email)
    job.applied_emails=s
    job.save()
    
    # notification
    obj=recruiters.objects.get(email=user_email)
    t=(job.name,user_email,str(job.id))
    notification.objects.create(doer=obj.id,action="showed interest",jobname="$#$?".join(t))
    return redirect("/home/")

def leavejob(request,id):
    user_email=request.COOKIES["user_email"]
    job=jobs.objects.get(id=id)
    a=job.applied_emails.split(",")
    a.remove(user_email)
    s=",".join(a)
    job.applied_emails=s
    job.save()
    return redirect("/home/")