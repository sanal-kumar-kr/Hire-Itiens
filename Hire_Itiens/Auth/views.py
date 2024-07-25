from django.shortcuts import render

from .forms import *
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.
def custom_404(request, exception):
    return render(request, '404.html', status=404)
def Register_page(request):
    return render(request, 'indexreg.html')

def userareg(request,ut):
    # try:
        if ut==0:
            form=RegJobSeakersForm(request.POST,request.FILES)
            if  request.method=="POST":
                if form.is_valid():
                        data=form.save(commit=False)
                        data.password = make_password(form.cleaned_data['password'])
                        data.usertype=0
                        data.status=1
                        data.save()    
                        messages.error(request, "Registeration Success")            
                        return redirect('/')    
            else:
                form=RegJobSeakersForm()
                return render(request,'Register.html',{'form':form,'user':'Job Seeker','ut':0})    
        elif ut==2:
            form=RegcompanyForm(request.POST,request.FILES)
            if  request.method=="POST":
                print("adgshfashsbfdsbgdsg")
                print(form.errors)
                if form.is_valid():
                    data=form.save(commit=False)
                    data.password = make_password(form.cleaned_data['password'])

                    data.usertype=2
                    data.status=0
                    data.save()    
                    messages.error(request, "Registeration Success")            

                    return redirect('/')    

            else:
                form=RegcompanyForm()
                return render(request,'Register.html',{'form':form,'user':'company','ut':2})  
        elif ut==3:
            form=RegcollegeForm(request.POST,request.FILES)
            if  request.method=="POST":
                print(form.is_valid())
                print(form.errors)

                if form.is_valid():
                    data=form.save(commit=False)
                    data.password = make_password(form.cleaned_data['password'])

                    data.usertype=3
                    data.status=0
                    data.save()
                    messages.error(request, "Registeration Success")            

                    return redirect('/')    

            else:
                form=RegcollegeForm()
                return render(request,'Register.html',{'form':form,'user':'college','ut':3})
    # except:
    #         return render(request,"Something_went_wrong.html")    

def login(request):
    # try:
        form = LoginForm()
        if request.method == "POST":
            user = authenticate(request,username=request.POST["username"],password=request.POST["password"] )
            if user is None :
                messages.error(request, "Invalid Username or Password!!!!!!!!!!!!")            
                return redirect('/login')

            elif user.status==1:
                auth_login(request, user)
                data = Register.objects.get(username=user)
                if data.is_superuser:
                    data.status=1
                    data.usertype=1
                    data.save()
                request.session['ut']=data.usertype

                data.usertype
                request.session['userid']=data.id
                request.session['islog']=True


                return redirect('/')
            elif user.status==0:
                messages.error(request, "Admin Not Approved Yet!!!!!!!!!!!!")            
                return redirect('/login')

     
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form}) 
    # except:
    #     return render(request,"Something_went_wrong.html")   

@login_required(login_url='/login')
def Logout(request):
    try:
        auth.logout(request)
        return redirect('/')
    except:
        return render(request,"Something_went_wrong.html")       
