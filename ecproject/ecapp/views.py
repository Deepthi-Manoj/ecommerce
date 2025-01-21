from django.shortcuts import render
from . models import  Banner_area
from . models import  Banner


# Create your views here.
def base(request):
    return render(request,'base.html')
def index(request):
    slider=Banner_area.objects.all()
   
    banner = Banner.objects.all()  # Fetch all Banner objects from the database
    context={'slider':slider,'banner': banner}
    return render(request,'index.html',context)
