
from .models import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages  # Import messages module
from .forms import *
# Create your views here.
@login_required(login_url='/login')
def sendrequests(request,id):
    try:
        if request.user.usertype == 0:
            form=jobrequestForm(request.POST,request.FILES)
            if request.method == "POST":
                if form.is_valid():
                    visitrequests.objects.create(
                                    user_id=Register.objects.get(id=request.user.id),
                                    Company_id=Register.objects.get(id=id),
                                    resume=form.cleaned_data['resume'],
                                    message=form.cleaned_data['message']

                                )
                    messages.error(request, "Requests Sended Successfuuly")            
                    return redirect('/users/2') 
            else:
                form=jobrequestForm()
                return render(request,'send_request.html',{'form':form}) 

        else:
            return render(request, 'permission_denied.html') 

    except:
        return render(request,"Something_went_wrong.html")



@login_required(login_url='/login')
def Applyjobs(request,id):
    try:
        if request.user.usertype == 0:
            form=Applyjobform(request.POST,request.FILES)
            if request.method == "POST":
                if form.is_valid():
                    Applyjos.objects.create(
                                    user_id=Register.objects.get(id=request.user.id),
                                    job_id=JobVaccancies.objects.get(id=id),
                                    resume=form.cleaned_data['resume'],
                                    cv=form.cleaned_data['cv']

                                )
                    messages.error(request, "Requests Sended Successfuuly")            
                    return redirect('/') 
            else:
                form=Applyjobform()
                return render(request, 'applyjob.html',{'form':form}) 

        else:
            return render(request, 'permission_denied.html') 

    except:
        return render(request,"Something_went_wrong.html")




@login_required(login_url='/login')
def applications(request):
    try:
        if request.user.usertype == 2:
            queryset = Applyjos.objects.filter(job_id__Company_id=request.user.id)
            return render(request, 'applications.html', {"data": queryset})   

        else:      
            queryset = Applyjos.objects.filter(user_id=request.user.id)
            return render(request, 'myapplications.html', {"data": queryset})   
    except:
        return render(request,"Something_went_wrong.html")  



@login_required(login_url='/login')
def savejob(request,id):
    try:
        if request.user.usertype == 0:
            uni=savedjobs.objects.filter(user_id=request.user.id,job_id=id).first()
            if uni:
                messages.error(request, "Already Added To Saved Jobs")    
                return redirect('/viewjobs')
            


            savedjobs.objects.create(
                user_id=Register.objects.get(id=request.user.id),    
                job_id=JobVaccancies.objects.get(id=id)
            )
            messages.error(request, " Added To Saved Jobs")    
            return redirect('/viewjobs')

        else:      
            return render(request, 'permission_denied.html')   
    except:
        return render(request,"Something_went_wrong.html")  



@login_required(login_url='/login')
def viewsaved(request):
    try:
        if request.user.usertype == 0:
            queryset = savedjobs.objects.filter(user_id=request.user.id)
            return render(request, 'saved_jobs.html', {"data": queryset}) 
           
        else:      
            return render(request, 'permission_denied.html')   
    except:
        return render(request,"Something_went_wrong.html")  



@login_required(login_url='/login')
def deletesavejob(request,id):
    try:
        if request.user.usertype == 0:
            queryset = savedjobs.objects.get(id=id)
            queryset.delete()
            messages.error(request, " Deleted Success Fully")    
            return redirect('/viewsaved')           
        else:      
            return render(request, 'permission_denied.html')   
    except:
        return render(request,"Something_went_wrong.html")  


@login_required(login_url='/login')
def cancelreq(request,id):
    try:
        if request.user.usertype == 0 or request.user.usertype == 2 or request.user.usertype == 3:
            queryset = visitrequests.objects.get(id=id)
            queryset.delete()
            messages.error(request, " Deleted Success Fully")    
            return redirect('/jobvisits')           
        else:      
            return render(request, 'permission_denied.html')   
    except:
        return render(request,"Something_went_wrong.html")  