from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import AbstractUser

GENDER=[
    
    ('Female','Female'),
    ('Male','Male'),
    ('Other','Other'),
]
MNCC=[
    ('Yes','Yes'),
    ('No','No'),
   
]
class Register(AbstractUser):
    gender = models.CharField(max_length=50,null=True,choices=GENDER)
    dob=models.CharField(max_length=50,default='')
    contact = models.IntegerField(null=True)
    address = models.TextField(null=True)
    usertype = models.IntegerField(null=True)
    status=models.IntegerField(null=True,default=1)
    profile=models.FileField(null=True)
    company_certificate=models.FileField(null=True)
    college_certificate=models.FileField(null=True)
    companyLicenceid=models.CharField(max_length=50,null=True)
    It_park_name=models.CharField(max_length=50,null=True)
    qualifications=models.TextField(null=True)
    uploadresume=models.FileField(null=True)
    country=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50,null=True)
    pincode=models.CharField(max_length=50,null=True)
    college_name=models.CharField(max_length=50,null=True)
    collegecode=models.CharField(max_length=50,null=True)
    passoutyear=models.CharField(max_length=50,null=True)
    skills=models.TextField(null=True)
    experience=models.CharField(max_length=300,null=True)
    college_section=models.CharField(max_length=300,null=True)
    number_of_students=models.CharField(max_length=300,null=True)
    company_desc=models.TextField(null=True)
    college_desc=models.TextField(null=True)
    MNC=models.CharField(max_length=50,null=True,choices=MNCC)
    


    
    