
from django import forms
from Company.models import *
from .models import *
class jobrequestForm(forms.ModelForm):
    class Meta:
        model = visitrequests
        fields = ['message','resume']
        widgets = {
            "message" : forms.Textarea(attrs={'class':'form-control','style':'height:50px'}),
            "resume" : forms.FileInput(attrs={'class':'form-control','style':'height:50px'}),

        }
    help_texts={
        'message':''
    }   



class Applyjobform(forms.ModelForm):
    class Meta:
        model = Applyjos
        fields = ['resume', 'cv']
        widgets = {
            'cv': forms.FileInput(attrs={'class': 'form-control', 'style': 'height:50px'}),
            'resume': forms.FileInput(attrs={'class': 'form-control', 'style': 'height:50px'}),
        }
        help_texts = {
            'cv': '',
            'resume': '',
        }
        labels = {
            'cv': 'Cover Letter',
            'resume': 'Resume',
        }