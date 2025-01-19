from django.shortcuts import render
from . models import  Banner_area

# Create your views here.
def base(request):
    return render(request,'base.html')
def index(request):
    banner=Banner_area.objects.all()
    context={'banner':banner}

    return render(request,'index.html',context)
