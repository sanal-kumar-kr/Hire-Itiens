
from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','password']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "password" : forms.PasswordInput(attrs={'class':'form-control','style':''})
        }
        help_texts = {
            'username' : None
        }
        
class RegJobSeakersForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password','email','gender','contact','address','profile','qualifications','experience','skills','uploadresume','country','state','district','city','pincode','college_name','collegecode','passoutyear']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'User Name......'}),
            "email" : forms.EmailInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Email....'}),
            "gender" : forms.Select(attrs={'class':'form-input','style':'width : 90%;','placeholder':''}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Contact.....'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Address...'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Password....'}),
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
            'password' : '',
        } 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  

     



       
class RegcompanyForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password','email','contact','address','MNC','It_park_name','profile','company_certificate','company_desc','companyLicenceid','country','state','district','city','pincode']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Company Name....'}),
            "email" : forms.EmailInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Email...'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Contact...'}),
             "MNC" : forms.Select(attrs={'class':'form-input','style':'width : 90%;','placeholder':'MNC....'}),
            "It_park_name" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'It Park Name...'}),
            "address" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Address..'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Password....'}),
            "profile" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Licence Id/Register Id Of Infrastructure'}),
            "company_certificate" : forms.FileInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Licence Id/Register Id Of Infrastructure'}),
            "company_desc" : forms.Textarea(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Company Description...'}),
            "companyLicenceid" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Licence Id/Register Id Of Infrastructure'}),
            "country" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Country...'}),
            "state" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'State....'}),
            "district" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'District...'}),
            "city" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'City...'}),
            "pincode" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Pincode....'}),
        }
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'experience' : '',
            'address' : '',
            'password' : '',
        } 
        labels={
          'company_desc' :'About The Company',
           
        }  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  

class RegcollegeForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password','email','contact','address','profile','college_certificate','college_desc','collegecode','state','country','district','city','pincode','college_section','number_of_students']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'College Name....'}),
            "email" : forms.EmailInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Email....'}),
            "contact" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Contact....'}),
            "address" : forms.TextInput(attrs={'class':'form-input','style':'width : 90%;height:100px','placeholder':'Address....'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 90%;','placeholder':'Password....'}),
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
            'password' : '',
        } 
        labels={
          'college_desc' :'About The College',
           
        }    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  
