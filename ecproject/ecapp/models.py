from django.db import models

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

    
      