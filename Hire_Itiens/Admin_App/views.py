from django.shortcuts import render
from Auth.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages

from django.db.models import Q
def custom_404(request, exception):
    return render(request, '404.html', status=404)
# Create your views here.
@login_required(login_url='/login')
def view_users(request,ut):
    try:
        if request.user.usertype == 1:
            search_query = request.GET.get('search_query')
            if ut == 0:
                queryset = Register.objects.filter(usertype=0, status=0)
            elif ut == 2: 
                queryset = Register.objects.filter(usertype=2, status=0)
            elif ut == 3:
                queryset = Register.objects.filter(usertype=3, status=0)
            
            if search_query:
                queryset = queryset.filter(
                    Q(username__icontains=search_query) |
                    Q(contact__icontains=search_query) |
                    Q(email__icontains=search_query) |
                    Q(college_desc__icontains=search_query) |
                    Q(address__icontains=search_query)
                )
            
            return render(request, 'View_user.html', {"ut": ut, "data": queryset})
        else:
            return render(request,"permission_denied.html")    
    except:
        return render(request,"Something_went_wrong.html")   

@login_required(login_url='/login')
def approve(request,id):
    try:
        if request.user.usertype == 1:
            user=Register.objects.get(id=id)
            user.status=1
            user.save()
            referring_url = request.META.get('HTTP_REFERER')
            return redirect(referring_url or '/')
        else:
            return render(request,"permission_denied.html")  
    except:
        return render(request,"Something_went_wrong.html")          
  

@login_required(login_url='/login')
def reject(request,id):
    try: 
        if request.user.usertype == 1:
            user=Register.objects.get(id=id)
            user.status=2
            user.save()
            referring_url = request.META.get('HTTP_REFERER')
            return redirect(referring_url or '/')
        else:
            return render(request,"permission_denied.html")
    except:
        return render(request,"Something_went_wrong.html")        
   
def view_app_users(request,ut):
    try:
        if request.user.usertype == 1:
            search_query = request.GET.get('search_query')
            if ut == 0:
                queryset=Register.objects.filter(usertype=0,status=1)
            elif ut  == 2: 
                queryset=Register.objects.filter(usertype=2,status=1)
            elif ut  == 3:
                queryset=Register.objects.filter(usertype=3,status=1)
            if search_query:
                queryset = queryset.filter(
                    Q(username__icontains=search_query) |
                    Q(contact__icontains=search_query) |
                    Q(email__icontains=search_query) |
                    Q(college_desc__icontains=search_query) |
                    Q(address__icontains=search_query)
                )    
            return render(request,'View_App_users.html',{"ut":ut,"data":queryset})  
        elif request.user.usertype == 0 or request.user.usertype == 3:
            print("Job Seakerssss")
            search_query = request.GET.get('search_query')
            if ut == 2: 
                queryset = Register.objects.filter(usertype=2, status=1)
            if search_query:
                queryset = queryset.filter(
                    Q(username__icontains=search_query) |
                    Q(contact__icontains=search_query) |
                    Q(email__icontains=search_query) |
                    Q(college_desc__icontains=search_query) |
                    Q(address__icontains=search_query)
                )
            return render(request, 'View_App_users.html', {"ut": ut, "data": queryset})    
        else:
            return render(request,"permission_denied.html")    
    except:
        return render(request,"Something_went_wrong.html")   

    
# Create your views here.
def Editcompany(request,id):
    # try:
        if request.user.usertype == 2:
            data = Register.objects.get(id=id)
            if request.method == 'POST':
                form = EditcompanyForm(request.POST,request.FILES,instance=data)  
                print(form.errors)
                if form.is_valid():
                    email = form.cleaned_data['email']
                    form.save()
                    messages.error(request, "Edited Successfuuly")            

                    return redirect('/')
            else:
                form = EditcompanyForm(instance=data)
            return render(request, 'Edit_Company.html', {'ur':"Company",'form': form})
        else:
            return render(request,"permission_denied.html")     
    # except:
    #     return render(request,"Something_went_wrong.html")  




def EditJobSeakers(request,id):
    # try:
        if request.user.usertype == 0:
            data = Register.objects.get(id=id)
            if request.method == 'POST':
                form = EditJobSeakersForm(request.POST,request.FILES,instance=data)    
                print(form.errors)

                if form.is_valid():
                    email = form.cleaned_data['email']
                    form.save()
                    messages.error(request, "Edited Successfuuly")            

                    return redirect('/')
            else:
                form = EditJobSeakersForm(instance=data)
            return render(request, 'Edit_JobSeakers.html', {'ur':"Job Seakers",'form': form})
        else:
            return render(request,"permission_denied.html")     
    # except:
    #     return render(request,"Something_went_wrong.html")  






def Editcollege(request,id):
    # try:
        if request.user.usertype == 3:
            data = Register.objects.get(id=id)
            if request.method == 'POST':
                form = EditcollegeForm(request.POST,request.FILES,instance=data) 
                print(form.errors)   
                if form.is_valid():
                    email = form.cleaned_data['email']
                    form.save()
                    messages.error(request, "Edited Successfuuly")            

                    return redirect('/')
            else:
                form = EditcollegeForm(instance=data)
            return render(request, 'Edit_College.html', {'ur':"College",'form': form})
        else:
            return render(request,"permission_denied.html")     
    # except:
    #     return render(request,"Something_went_wrong.html")

def Deleteuser(request,id):
    try:
        if request.user.usertype == 1:
            data=Register.objects.get(id=id)
            referring_url = request.META.get('HTTP_REFERER')
            data.delete()
            return redirect(referring_url or '/')
        else:
            return render(request,"permission_denied.html")     
    except:
        return render(request,"Something_went_wrong.html")

def usersreq_int(request):
    try:
        return render(request,"userreq_interface.html")
    except:
        return render(request,"Something_went_wrong.html")



def users_int(request):
    try:
        return render(request,"user_interface.html")
    except:
        return render(request,"Something_went_wrong.html")