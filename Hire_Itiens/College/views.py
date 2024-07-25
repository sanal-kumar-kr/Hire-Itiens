from Company.models import *
from .forms import*
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
# Create your views here.
@login_required(login_url='/login')
def crequest(request,id):
    try:
        if request.user.usertype == 3:
            form=requestForm(request.POST,request.FILES)
            if request.method == "POST":
                if form.is_valid():
                    visitrequests.objects.create(
                                    user_id=Register.objects.get(id=request.user.id),
                                    message=form.cleaned_data['message'],
                                    Company_id=Register.objects.get(id=id)
                                )
                    messages.error(request, "Requests Sended Successfuuly")            
                    return redirect('/users/2') 
            else:
                  form=requestForm()
                  return render(request, 'send_request.html',{'form':form}) 
        else:
            return render(request, 'permission_denied.html') 

    except:
        return render(request,"Something_went_wrong.html")  