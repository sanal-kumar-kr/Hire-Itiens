from django.db import models
from django.utils import timezone
from Auth.models import *
from django.utils import timezone

# Create your models here.
class JobVaccancies(models.Model):
    title=models.CharField(max_length=250,default='')
    numofpos=models.IntegerField(null=True)
    qualification=models.CharField(max_length=250,default='')
    Location=models.CharField(max_length=250,default='')
    current_date = models.DateTimeField(default=timezone.now)
    experience=models.TextField(default='')
    jobdesc=models.TextField(default='')
    jobreq=models.TextField(default='')
    interviewtime=models.TimeField(null=True)
    interviewdate=models.DateField(null=True)
    int_type=models.IntegerField(null=True)
    Company_id= models.ForeignKey(Register,related_name='company',on_delete=models.CASCADE, null=True)

class interships(models.Model):
    title=models.CharField(max_length=250,default='')
    desc=models.TextField(default='')
    duration=models.CharField(max_length=250,default='')
    Company_id= models.ForeignKey(Register,related_name='companyid',on_delete=models.CASCADE, null=True)
    int_type=models.IntegerField(null=True)

    
class visitrequests(models.Model):
    user_id= models.ForeignKey(Register,related_name='userv',on_delete=models.CASCADE, null=True)
    current_date=models.DateTimeField(default=timezone.now)
    Company_id= models.ForeignKey(Register,related_name='companyidv',on_delete=models.CASCADE, null=True)
    message=models.TextField(default='')
    resume=models.FileField(null=True)






class inbox(models.Model):
    sender = models.ForeignKey(Register, related_name='service_person', on_delete=models.CASCADE, null=True)
    reciever = models.ForeignKey(Register, related_name='org_id', on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)
    datetime=models.DateTimeField(null=True)
    status = models.IntegerField(null=True, default=0)

class request_chat(models.Model):
    sender = models.ForeignKey(Register, related_name='ds', on_delete=models.CASCADE, null=True)
    reciever = models.ForeignKey(Register, related_name='dsd', on_delete=models.CASCADE, null=True)
    status=models.IntegerField(null=True,default=0)
    status = models.IntegerField(null=True, default=0)









