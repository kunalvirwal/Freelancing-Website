from django.db import models
from . import *

# Create your models here.
class recruiters(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    profession=models.CharField(max_length=30)
    org=models.TextField()
    role=models.CharField(max_length=20)
    profile_pic=models.ImageField(upload_to="Profile_pics")
    address=models.TextField()
    password=models.TextField()
    about=models.TextField()
    following=models.TextField()
    
class jobs(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    time=models.IntegerField()
    pay=models.IntegerField()
    quantity=models.CharField(max_length=30)
    rec=models.EmailField()
    applied_emails=models.TextField()
    
class notification(models.Model):
    doer=models.IntegerField()
    action=models.TextField()
    jobname=models.TextField()