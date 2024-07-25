from django.db import models
from django.utils import timezone
from Auth.models import *
from Company.models import *

# Create your models here.
class Applyjos(models.Model):
    user_id= models.ForeignKey(Register,related_name='rcv',on_delete=models.CASCADE, null=True)
    current_date=models.DateTimeField(default=timezone.now)
    job_id= models.ForeignKey(JobVaccancies,related_name='cvc',on_delete=models.CASCADE, null=True)
    resume=models.FileField(null=True)
    cv=models.FileField(null=True)
    
class savedjobs(models.Model):
    user_id= models.ForeignKey(Register,related_name='u',on_delete=models.CASCADE, null=True)
    current_date=models.DateTimeField(default=timezone.now)
    job_id= models.ForeignKey(JobVaccancies,related_name='j',on_delete=models.CASCADE, null=True)
