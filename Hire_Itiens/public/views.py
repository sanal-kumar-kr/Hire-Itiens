from django.shortcuts import render

# Create your views here.
def custom_404(request, exception):
    return render(request, 'Something_went_wrong.html', status=404)
def index(request):
    # try:
        return render(request,'index.html')
    # except:
        # return render(request,"Something_went_wrong.html")       
def about(request):
    try:
        return render(request,'about.html')
    except:
        return render(request,"Something_went_wrong.html")       
def contact(request):
    try:
        return render(request,'contact.html')
    except:
        return render(request,"Something_went_wrong.html")       
def services(request):
    try:
        return render(request,'service.html')
    except: 
        return render(request,"Something_went_wrong.html")   
