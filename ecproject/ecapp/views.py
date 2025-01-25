from django.shortcuts import render
from . models import  Banner_area
from . models import  Banner
from . models import  Main_Category
from . models import  Product


# Create your views here.
def base(request):
    return render(request,'base.html')
def index(request):
    slider=Banner_area.objects.all()
   
    banner = Banner.objects.all()  # Fetch all Banner objects from the database
    category=Main_Category.objects.all()

    Products=Product.objects.all()


    context={'slider':slider,'banner': banner,'category':category,'products':Products }
    return render(request,'index.html',context)
