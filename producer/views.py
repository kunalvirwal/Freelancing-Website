from django.shortcuts import render,redirect
from producer.models import *
# Create your views here.

def producer_info(request,obj):
    l=[]
    for i in jobs.objects.filter(rec=obj.email):
        a={"guy":i.name,"discription":i.desc,"hours":i.time,"price":i.pay,"quantity":i.quantity,"id":i.id}
        l.append(a)    #  jobs opened
        
    params={  
        "name":obj.name,
        "about":obj.about,
        "profile_pic":obj.profile_pic,
        "email":obj.email,
        "phone":obj.phone,
        
        "profession":obj.profession,
        "org":obj.org,
        "address":obj.address,
        "jobs":l
        
    }
    
    response=render(request,"producer_profile.html",params)
    response.set_cookie('user_email', obj.email)  
    response.set_cookie('user_role', obj.role)
    return response


def  newjob(request):
    if request.method=="POST":
        data=request.POST
        g=data.get("guy")
        disc=data.get("discription")
        hrs=data.get("hours")
        prc=data.get("price")
        q=data.get("quantity")
        em  = request.COOKIES['user_email']  
    
        hrs=hrs.strip()
        prc=prc.strip()
        if hrs!='' and prc!='':
            jobs.objects.create(name=g,desc=disc,time=hrs,pay=prc,quantity=q,rec=em,applied_emails="")
        
            # for notifications
            obj=recruiters.objects.get(email=em)
            notification.objects.create(doer=obj.id,action="added a new job",jobname=g)
        
        return redirect("/home/")
    return render(request,"new_job.html")

def delete_job(request,id):
    s=jobs.objects.get(id=id)
    
    # for notifications
    em  = request.COOKIES['user_email']  
    obj=recruiters.objects.get(email=em)
    notification.objects.create(doer=obj.id,action="removed the job",jobname=s.name)
    
    s.delete()
    return redirect("/home/")

def edit_profile(request):
    
    user_email  = request.COOKIES['user_email']  
    obj=recruiters.objects.get(email=user_email)
    params={"name":str(obj.name),
            "email":str(obj.email),
            "phn":str(obj.phone),
            "profession":str(obj.profession),
            "org":str(obj.org),
            "address":str(obj.address),
            "password":str(obj.password),
            "about":str(obj.about)}
    
    if request.method=="POST":
        data=request.POST
        n=data.get("name")
        phn=data.get("phn")
        prof=data.get("profession")
        o=data.get("org")
        add=data.get("address")
        passw=data.get("password")
        ab=data.get("about")
        profile=request.FILES.get("profile_pic")
        
        s=recruiters.objects.get(email=obj.email)
        if profile:
            s.profile_pic=profile

        
        s.name=n
        s.phone=phn
        s.profession=prof
        s.org=o
        s.address=add
        s.password=passw
        s.about=ab
        s.save()
        return redirect("/home/")
    
    
    return render(request,"editprofile.html",params)

def jobpage(request,id):
    job=jobs.objects.get(id=id)
    s=recruiters.objects.get(email=job.rec)
    user_email  = request.COOKIES['user_email']  
    obj=recruiters.objects.get(email=user_email)
    
    l=[]
    a=job.applied_emails.split(",")
    print(a)
    if len(a)!=0:
        for i in a:
            if i!='':
                j=recruiters.objects.get(email=i)
                l.append(j)
        
        
    params={
        "guy":job.name,
        "quant":job.quantity,
        "prc":job.pay,
        "hrs":job.time,
        "desc":job.desc,
        "sid":s.id,
        "selfid":obj.id,
        "opener":s.name,
        "pic":s.profile_pic,
        "email":s.email,
        "phn":s.phone,
        "people":l
    }
    return render(request,"jobpage.html",params)


def freelancer_list(request):
    people=recruiters.objects.filter(role="Freelancer")
    return render(request,"freelancerlist.html",{"people":people,})