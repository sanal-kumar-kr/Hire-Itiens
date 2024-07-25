
from django import forms
from .models import *

INT_CHOICES = [
        ('', '--------------------Select Interview Type--------------------------------------'),
        ('2', 'Online'),
        ('3', 'Offline'),
    ]
class AddVaccancyForm(forms.ModelForm):
    class Meta:
        model = JobVaccancies
        fields = ['title','qualification','experience','numofpos','jobdesc','jobreq']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "qualification" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobdesc" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobreq" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "experience" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "numofpos" : forms.TextInput(attrs={'class':'form-control','style':''})
        }
        labels={
          'jobdesc' :'About The Job',
           'jobreq' :'Job requirements',
            'experience' :'Required Experience',
            'numofpos' :'Number Of Positions',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  

class AddInterviewForm(forms.ModelForm):
    Interview_Type = forms.ChoiceField(choices=INT_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}))

    class Meta:
        model = JobVaccancies
        fields = ['title','qualification','experience','jobdesc','jobreq','interviewdate','interviewtime','Location']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "qualification" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobdesc" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobreq" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "experience" : forms.Textarea(attrs={'class':'form-control','style':'height:100px','col':'5'}),
            "interviewdate" : forms.DateInput(attrs={'class':'form-control','style':'','type':'date'}),
            "interviewtime" : forms.TimeInput(attrs={'class':'form-control','style':'','type':'time'}),
            "Location" : forms.TextInput(attrs={'class':'form-control','style':''}),
        }
        labels={
          'jobdesc' :'About The Job',
           'jobreq' :'Job requirements',
            'experience' :'Required Experience',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  


class AddInternshipForm(forms.ModelForm):
    class Meta:
        model = interships
        fields = ['title','desc','duration']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "desc" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "duration" : forms.TextInput(attrs={'class':'form-control','style':''}),

        }
        labels={
          'desc' :'About The Program',
           
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  

class EditVaccancyForm(forms.ModelForm):
    class Meta:
        model = JobVaccancies
        fields = ['title','qualification','experience','numofpos','jobdesc','jobreq']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "qualification" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobdesc" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobreq" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "experience" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "numofpos" : forms.TextInput(attrs={'class':'form-control','style':''})
        }
        labels={
          'jobdesc' :'About The Job',
           'jobreq' :'Job requirements',
            'experience' :'Required Experience',
            'numofpos' :'Number Of Positions',
        }



class EditInterviewForm(forms.ModelForm):

    class Meta:
        model = JobVaccancies
        fields = ['title','qualification','experience','jobdesc','jobreq','interviewdate','interviewtime',"Location"]
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "qualification" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobdesc" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "jobreq" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "experience" : forms.Textarea(attrs={'class':'form-control','style':'height:100px','col':'5'}),
            "interviewdate" : forms.DateInput(attrs={'class':'form-control','style':'','type':'date'}),
            "interviewtime" : forms.TimeInput(attrs={'class':'form-control','style':'','type':'time'}),
            "Location" : forms.TextInput(attrs={'class':'form-control','style':''}),

        }
        labels={
          'jobdesc' :'About The Job',
            'jobreq' :'Job requirements',
            'experience' :'Required Experience',
        }




class EditInternshipForm(forms.ModelForm):
    class Meta:
        model = interships
        fields = ['title','desc','duration']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "desc" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "duration" : forms.TextInput(attrs={'class':'form-control','style':''}),

        }
        labels={
          'desc' :'About The Program',
            
        }


class messageform(forms.ModelForm):
    
    class Meta:
        model = inbox
        fields = ['message']
        widgets = {
            "message" : forms.Textarea(attrs={'class':'form-control','style':'height :50px;'}),
        }
        help_texts = {
            'message' : None
        }