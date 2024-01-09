from django.shortcuts import render, redirect
from producer.models import *

# Create your views here.
# A new app for authentication

def signin(request):
    
    
    if request.method=="POST":
        
        data=request.POST
        n=data.get("name").strip()
        e=data.get("email").strip()
        phn=data.get("phn").strip()
        prof=data.get("profession").strip()
        o=data.get("org").strip()
        add=data.get("address").strip()
        passw=data.get("password").strip()
        r=data.get("role")
        ab=data.get("about").strip()
        profile=request.FILES.get("profile_pic")
        
            
        if not(n=='' or e=='' or phn=='' or len(phn)!=10 or add=='' or passw==''):
            s=recruiters.objects.create(name=n,
                                    email=e,
                                    phone=phn,
                                    profession=prof,
                                    org=o,
                                    role=r,
                                    profile_pic='',
                                    address=add,
                                    password=passw,
                                    about=ab) 
            if profile:
                s.profile_pic=profile  
            else:
                s.profile_pic="Profile_pics/user.png"
            s.save()
            
        return redirect('/')
        
    return render(request,"signup.html")

