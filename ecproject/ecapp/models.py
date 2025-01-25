from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
 

# Create your models here.
class Banner_area(models.Model):
    
    title = models.CharField(max_length=200,default="")
    image=  models.ImageField(upload_to='bannertop')
    deal= models.CharField(max_length=50,default="")
    sale= models.IntegerField()
    discount= models.IntegerField()
    link= models.CharField(max_length=100,default="")

    def __str__(self):
        return self.title
    
class Main_Category(models.Model):
    name = models.CharField(max_length=100,default="")  

    def __str__(self):
        return self.name
    
class Category(models.Model):
    main_Category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name
    
class Sub_Category(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="")   

    def __str__(self):
        return self.name 
    
class Banner(models.Model):
    image = models.ImageField(upload_to='banner')    
    title = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.title
class Product(models.Model):
    name = models.CharField(max_length=200,default="")
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField(default=0,null=True)
    discount = models.PositiveIntegerField(default=0,null=True)
    featured_image = models.CharField(max_length=200,default="")
    brand = models.CharField(max_length=200,null=True)
    total = models.PositiveIntegerField(default=0,null=True)
    available = models.PositiveIntegerField(default=0,null=True)
    image=models.ImageField(null=True,blank=True)
   
    description= RichTextField(null=True,blank=True)
    product_information = RichTextField(null=True,blank=True)
    tags =  models.CharField(max_length=200,default="")
    slug = models.CharField(max_length=555,null=True,blank=True)

    def __str__(self):
        return self.name
    
def generate_slug():
    pass    

@receiver(pre_save,sender=Product)
def generate_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        base_slug = slugify(instance.name)
        unique_slug = base_slug
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{instance.id}"
        instance.slug=unique_slug    

class Additional_information(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)    
    spec = models.CharField(max_length=255,null=True,blank=True)  

class Additional_image(models.Model):
     Product = models.ForeignKey(Product,on_delete=models.CASCADE)
     images = models.CharField(max_length=255,null=True,blank=True)

