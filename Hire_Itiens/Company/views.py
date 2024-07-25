from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages  # Import messages module
from itertools import chain

from Auth.models import *
def custom_404(request, exception):
    return render(request, '404.html', status=404)
# Create your views here.
def postjobs(request):
    try:
        if request.user.usertype == 2:
            form=AddVaccancyForm(request.POST,request.FILES)
            if  request.method=="POST":
                if form.is_valid():
                    JobVaccancies.objects.create(
                        title=form.cleaned_data['title'],
                        qualification=form.cleaned_data['qualification'],
                        jobdesc=form.cleaned_data['jobdesc'],
                        jobreq=form.cleaned_data['jobreq'],
                        experience=form.cleaned_data['experience'],
                        int_type=1,
                        Company_id=Register.objects.get(id=request.user.id),
                        numofpos=form.cleaned_data['numofpos'],
                    )
                    return redirect('/')    
            else:
                form=AddVaccancyForm()
                return render(request,'Add_JobVaccancy.html',{'form':form,'title':'Add Job Vaccancy','postjobs':True}) 
        else:
            return render(request,"permission_denied.html")           
    except:
        return render(request,"Something_went_wrong.html")   



def AddIntervies(request):
    try:
        if request.user.usertype == 2:
            form=AddInterviewForm(request.POST,request.FILES)
            if  request.method=="POST":
                print(form.errors)
                print(form.is_valid())
                if form.is_valid():
                    JobVaccancies.objects.create(
                        interviewtime=form.cleaned_data['interviewtime'],
                        interviewdate=form.cleaned_data['interviewdate'],
                        Location=form.cleaned_data['Location'],
                        experience=form.cleaned_data['experience'],
                        jobreq=form.cleaned_data['jobreq'],
                        jobdesc=form.cleaned_data['jobdesc'],
                        title=form.cleaned_data['title'],
                        int_type=form.cleaned_data['Interview_Type'],
                        Company_id=Register.objects.get(id=request.user.id),
                        qualification=form.cleaned_data['qualification'],
                    )
                    return redirect('/')    
            else:
                form=AddInterviewForm()
                return render(request,'Add_JobVaccancy.html',{'form':form,'title':'Add Interview','validate':True}) 
        else:
            return render(request,"permission_denied.html")           
    except:
        return render(request,"Something_went_wrong.html")   



def addprograms(request,t):
    try:
        if request.user.usertype == 2:
            form=AddInternshipForm(request.POST,request.FILES)
            if  request.method=="POST":
                print(form.errors)
                if form.is_valid():
                    interships.objects.create(
                        duration=form.cleaned_data['duration'],
                        desc=form.cleaned_data['desc'],
                        title=form.cleaned_data['title'],
                        Company_id=Register.objects.get(id=request.user.id),
                        int_type=t
                    )
                    return redirect('/')    
            else:
                form=AddInternshipForm()
                if t == 1:
                    tl="Add Internship"
                else:
                    tl="Add Training"
                return render(request,'Add_JobVaccancy.html',{'form':form,'title':tl,'program':True}) 
        else:
            return render(request,"permission_denied.html")           
    except:
        return render(request,"Something_went_wrong.html")           



@login_required(login_url='/login')
def viewjobs(request):
    try:
        if request.user.usertype == 2:
            search_query = request.GET.get('search_query')
            queryset = JobVaccancies.objects.filter(Company_id=request.user.id,int_type=1)
            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(experience__icontains=search_query) 
                )
        else:       
            search_query = request.GET.get('search_query')
            queryset = JobVaccancies.objects.filter(int_type=1)
            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(experience__icontains=search_query) 
                )
        return render(request, 'View_JobVaccancies.html', {"data": queryset})   
    except:
        return render(request,"Something_went_wrong.html")  



@login_required(login_url='/login')
def ViewIntervies(request):
    try:
        if request.user.usertype == 2:
            search_query = request.GET.get('search_query')
            queryset = JobVaccancies.objects.filter(Q(int_type=2) | Q(int_type=3),Company_id=request.user.id)
            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(experience__icontains=search_query) |
                    Q(interviewdate__icontains=search_query) 

                )
        else:         
            search_query = request.GET.get('search_query')
            queryset = JobVaccancies.objects.filter(Q(int_type=2) | Q(int_type=3))
            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(experience__icontains=search_query) |
                    Q(interviewdate__icontains=search_query) 
                )
        return render(request, 'View_Interviews.html', { "data": queryset})   
    except:
        return render(request,"Something_went_wrong.html")  



@login_required(login_url='/login')
def viewprograms(request,t):
    try:
        if request.user.usertype == 2:
            search_query = request.GET.get('search_query')
            queryset = interships.objects.filter(Company_id=request.user.id,int_type=t)
            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(duration__icontains=search_query) 
                )
        else:      
            search_query = request.GET.get('search_query')
            queryset = interships.objects.filter(int_type=t)
            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(duration__icontains=search_query) 
                )
        if t == 1:
            tl="Internship Programs" 
        else:
            tl="Training Programs"

        return render(request, 'View_Intership.html', {"data": queryset,'title':tl})   
    except:
        return render(request,"Something_went_wrong.html")  



@login_required(login_url='/login')
def jobvisits(request):
    try:
        if request.user.usertype == 2:
            queryset = visitrequests.objects.filter(user_id__usertype=0)
            return render(request, 'view_job_req.html', {"data": queryset})   
        else:      
            queryset = visitrequests.objects.filter(user_id=request.user.id)
            return render(request, 'view_job_req_user.html', {"data": queryset})   

       
    except:
        return render(request,"Something_went_wrong.html")  


@login_required(login_url='/login')
def collegereq(request):
    try:
        if request.user.usertype == 2:
            queryset = visitrequests.objects.filter(user_id__usertype=3)
            return render(request, 'view_college_req.html', {"data": queryset})   

        else:      
            queryset = visitrequests.objects.filter(user_id=request.user.id)
            return render(request, 'view_college_req_college.html', {"data": queryset})   

    except:
        return render(request,"Something_went_wrong.html")  









def editprogram(request,id):
    try:
        if request.user.usertype == 2:
            data = interships.objects.get(id=id)
            if request.method == 'POST':
                form = EditInternshipForm(request.POST,request.FILES,instance=data)    
                if form.is_valid():
                    form.save()
                    return redirect('/')
            else:
                form = EditInternshipForm(instance=data)
            return render(request, 'edit_job.html', {'ur':"Edit Internship",'form': form})
        else:
            return render(request,"permission_denied.html")     
    except:
        return render(request,"Something_went_wrong.html")




def interviewedit(request,id):
    try:
        if request.user.usertype == 2:
            data = JobVaccancies.objects.get(id=id)
            if request.method == 'POST':
                form = EditInterviewForm(request.POST,request.FILES,instance=data)    
                if form.is_valid():
                    form.save()
                    return redirect('/ViewInterviews')
            else:
                form = EditInterviewForm(instance=data)
            return render(request, 'edit_job.html', {'ur':"College",'form': form})
        else:
            return render(request,"permission_denied.html")     
    except:
        return render(request,"Something_went_wrong.html")


def vaccancieedit(request,id):
    try:
        if request.user.usertype == 2:
            data = JobVaccancies.objects.get(id=id)
            if request.method == 'POST':
                form = EditVaccancyForm(request.POST,request.FILES,instance=data)    
                if form.is_valid():
                    form.save()
                    return redirect('/viewjobs')
            else:
                form = EditVaccancyForm(instance=data)
            return render(request, 'edit_job.html', {'ur':"Edit Vaccancie",'form': form})
        else:
            return render(request,"permission_denied.html")     
    except:
        return render(request,"Something_went_wrong.html")


@login_required(login_url='/login')
def deleteprogram(request,id):
    try:
        if request.user.usertype == 2:
            queryset = interships.objects.get(id=id)
            referring_url = request.META.get('HTTP_REFERER')
            queryset.delete()
            return redirect(referring_url or '/')
        else:
            return render(request,"permission_denied.html") 
    except:
        return render(request,"Something_went_wrong.html")  



@login_required(login_url='/login')
def deleteinterview(request,id):
    try:
        if request.user.usertype == 2:
            queryset = JobVaccancies.objects.get(id=id)
            referring_url = request.META.get('HTTP_REFERER')
            queryset.delete()
            return redirect(referring_url or '/')

        else:
            return render(request,"permission_denied.html") 
    except:
        return render(request,"Something_went_wrong.html")  


@login_required(login_url='/login')
def request_int(request):
    try:
       return render(request,"requests_interfaces.html") 
    except:
        return render(request,"Something_went_wrong.html")  


@login_required(login_url='/login')
def deletevaccancie(request,id):
    try:
        if request.user.usertype == 2:
            queryset = JobVaccancies.objects.get(id=id)
            referring_url = request.META.get('HTTP_REFERER')
            queryset.delete()
            return redirect(referring_url or '/')
        else:
            return render(request,"permission_denied.html") 
    except:
        return render(request,"Something_went_wrong.html")  

def sendchatrequest(request,cid):
    request_chat.objects.create(
        sender=request.user,
        reciever=Register.objects.get(id=cid)
    )
    messages.error(request, "Requests Sended Successfuuly")            

    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')


def acceptchatrequest(request,id):
    data=request_chat.objects.get(id=id)
    data.status=1
    data.save()
    messages.error(request, "Requests Accepted Successfuuly")            

    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')


def viewchatreq(request):
    data=request_chat.objects.filter(reciever=request.user.id,status=0)
    return render(request,'view_chat_req.html',{'data':data})

def viewchatusers(request):
    if request.user.usertype == 3:
        data=request_chat.objects.filter(sender=request.user.id,status=1)
    elif request.user.usertype == 2:
        data=request_chat.objects.filter(reciever=request.user.id,status=1)
    print(data)
    return render(request,'message_index.html',{'data':data})

def viewcompany(request):
    data=Register.objects.filter(usertype=2,status=1)
    return render(request,'view_req_companies.html',{'data':data})   


def message(request,id):
     
    if request.method=='POST':
        form = messageform(request.POST,request.FILES)
       
        if form.is_valid():
            print("valid")
            
            inbox.objects.create(
                sender =Register.objects.get(id=request.user.id),
                reciever = Register.objects.get(id=id),
                message = form.cleaned_data["message"],
                datetime=timezone.now()
                )
          
            data1=inbox.objects.filter(sender=request.user.id,reciever=id)
            data2=inbox.objects.filter(sender=id,reciever=request.user.id)
            merged_data = list(chain(data1, data2))
            merged_data.sort(key=lambda x: x.datetime) 
            return render(request,'chat_interface.html',{'data':merged_data,'form':form})
    else:
        form = messageform()
        data1=inbox.objects.filter(sender=request.user.id,reciever=id)
        data2=inbox.objects.filter(sender=id,reciever=request.user.id)
        merged_data = list(chain(data1, data2))
        merged_data.sort(key=lambda x: x.datetime) 
        print(merged_data)
    return render(request,'chat_interface.html',{'form':form,'data':merged_data})