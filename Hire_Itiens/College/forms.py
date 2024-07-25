
from Company.models import *
from django import forms
from .models import *

class requestForm(forms.ModelForm):
    class Meta:
        model = visitrequests
        fields = ['message']
        widgets = {
            "message" : forms.Textarea(attrs={'class':'form-control','style':'height:50px'}),
        }
    help_texts={
        'message':''
    }   
  