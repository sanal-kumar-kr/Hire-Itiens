

from django import forms
from Auth.models import *


class EditcompanyForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','email','contact','address','MNC','It_park_name','profile','company_certificate','company_desc','companyLicenceid','country','state','district','city','pincode']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Company Name....'}),
            "email" : forms.EmailInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Email...'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Contact...'}),
             "MNC" : forms.Select(attrs={'class':'form-input','style':'width : 90%;','placeholder':'MNC....'}),
            "It_park_name" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'It Park Name...'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Address..'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Licence Id/Register Id Of Infrastructure'}),
            "company_certificate" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Licence Id/Register Id Of Infrastructure'}),
            "company_desc" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Company Description...'}),
            "companyLicenceid" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Licence Id/Register Id Of Infrastructure'}),
            "country" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Country...'}),
            "state" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'State....'}),
            "district" : forms.TextInput(attrs={'class':'form-input','style':'width :90%;','placeholder':'District...'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'City...'}),
            "pincode" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Pincode....'}),
        }
        help_texts = {
            'username' : None,  
            'email' : '',
            'contact' : '',
            'experience' : '',
            'address' : '',
        } 
        def clean_company_certificate(self):
            company_certificate = self.cleaned_data.get('company_certificate')
            if not company_certificate:
                return None
            return company_certificate
        def clean_profile(self):
            profile = self.cleaned_data.get('profile')
            if not profile:
                return None
            return profile    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['pincode'].required = False  

class EditcollegeForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','email','contact','address','profile','college_certificate','college_desc','collegecode','state','country','district','city','pincode','college_section','number_of_students']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'College Name....'}),
            "email" : forms.EmailInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Email....'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Contact....'}),
            "address" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Address....'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "college_certificate" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "college_desc" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'College Description....'}),
            "collegecode" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'College code....'}),
             "country" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Country...'}),
            "state" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'State....'}),
            "district" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'District...'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'City...'}),
            "pincode" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Pincode....'}),
            "college_section" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'College Section....'}),
            "number_of_students" : forms.NumberInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Number Of Students....'}),
        }
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'experience' : '',
            'address' : '',
        }    
        def clean_college_certificate(self):
            college_certificate = self.cleaned_data.get('college_certificate')
            if not college_certificate:
                return None
            return college_certificate  
        def clean_profile(self):
            profile = self.cleaned_data.get('profile')
            if not profile:
                return None
            return profile               
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['pincode'].required = False  
class EditJobSeakersForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','email','gender','contact','address','profile','qualifications','experience','skills','uploadresume','country','state','district','city','pincode','college_name','collegecode','passoutyear']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'User Name......'}),
            "email" : forms.EmailInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Email....'}),
            "gender" : forms.Select(attrs={'class':'form-input','style':'width : 90%;','placeholder':''}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Contact.....'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Address...'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':''}),
            "uploadresume" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':''}),
            "country" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Country.....'}),
            "state" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'State.....'}),
            "district" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'District....'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'City....'}),
            "pincode" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Pincode.....'}),
            "college_name" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'College Name....'}),
            "collegecode" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'College Code'}),
            "passoutyear" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Passout Year'}),
            "qualifications" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':''}),
            "experience" : forms.TextInput(attrs={'class':'form-input','style':'width :90%;','placeholder':'Experience'}),
            "skills" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Skills'}),
        }
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'experience' : '',
            'address' : '',
        } 
        def clean_profile(self):
            profile = self.cleaned_data.get('profile')
            if not profile:
                return None
            return profile

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['pincode'].required = False    


