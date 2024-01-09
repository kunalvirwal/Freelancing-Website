from django.shortcuts import render
from producer.models import *
from producer.views import *
from freelancer.views import *

def login(request):
    
    if request.method=="POST":
        data=request.POST
        e=data.get("email")
        passw=data.get("password")
        s=recruiters.objects.all()
        if e=="k@k" and passw=="k":
            return admin_info(request)
        for i in s:
            if i.email==e and i.password==passw:
                if i.role=="Recruiter":
                    return producer_info(request,i)
                if i.role=="Freelancer":
                    return freelancer_info(request,i)
    
    response=render(request,"login.html")
    response.delete_cookie("user_login")
    response.delete_cookie("user_email")        
    return response

def home(request):
    
    user_email  = request.COOKIES['user_email']  
    user_role = request.COOKIES['user_role']
    obj=recruiters.objects.get(email=user_email)
    
    if user_role=="Recruiter":
        return producer_info(request,obj)
    if user_role=="Freelancer":
        return freelancer_info(request,obj)
    
    
def homeview(request,id):
    obj=recruiters.objects.get(id=id)
    l=[]
    user_role = request.COOKIES['user_role']
    if obj.role=="Recruiter":
        for i in jobs.objects.filter(rec=obj.email):
            a={"guy":i.name,"discription":i.desc,"hours":i.time,"price":i.pay,"quantity":i.quantity,"id":i.id}
            l.append(a)    #  jobs opened
            
    elif obj.role=="Freelancer":
        job=jobs.objects.all()
        for i in job:
            a=i.applied_emails.split(",")
            if obj.email in a:
                j=recruiters.objects.get(email=i.rec)
                l.append([i,j])
                
    params={  
        "name":obj.name,
        "about":obj.about,
        "profile_pic":obj.profile_pic,
        "email":obj.email,
        "phone":obj.phone,
        "selfrole":user_role,
        "role":obj.role,
        "profession":obj.profession,
        "org":obj.org,
        "address":obj.address,
        "jobs":l    
    }
    
    return render(request,"viewprofile.html",params)

def notifications(request):
    
    user_email = request.COOKIES['user_email']
    
    notifications=notification.objects.all()
    a=[]
    obj=recruiters.objects.get(email=user_email) # current user
    
    for i in notifications:
        person=recruiters.objects.get(id=i.doer)   #doer
        
        if person.id==obj.id :   # if current user is the doer
            k=i.jobname.split("$#$?")
            job_name=k[0]            # name of the interested job
            a.insert(0,[{"doer":i.doer,"action":i.action,"jobname":job_name},"You"])   ## takes only selected valuees and also reverses the list  [notification,doer reference]
            # if obj.role =="Freelancer":
            #     a.insert(0,[{"doer":i.doer,"action":i.action,"jobname":job_name},"You"])   ## takes only selected valuees and also reverses the list  [notification,doer reference]
            # elif obj.role =="Recruiter":
            #     a.insert(0,[{"doer":i.doer,"action":i.action,"jobname":job_name},"You"])   ## takes only selected valuees and also reverses the list  [notification,doer reference]
        elif i.action=="showed interest":
            k=i.jobname.split("$#$?")
            job_name=k[0]            # name of the interested job
            print(k,"\n", job_name)
            em=k[1]         #  email of the freelancer who was interested
            job_id=k[2]     # the job id to select only those jobs which belong to the current user
            job=jobs.objects.get(id=job_id)
            free=recruiters.objects.get(email=em)
            if job.rec == user_email: 
                a.insert(0,[{"doer":i.doer,"action":i.action,"jobname":job_name},free.name])
                
                
                
                
        # if obj.following!='':## if current user is a follower of the doer
        #     b=[int(i) for i in obj.following.split(",")]
        #     if person.id in b:
        #         a.insert(0,[i,person.name])

    params={"notify":a,
            "self":obj}
    
    return render(request,"notifications.html",params)

def admin_info(request):
    
    params={"people":recruiters.objects.all()}
        
    return render(request,"Admin.html",params)