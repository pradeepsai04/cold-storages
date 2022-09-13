from email.policy import default
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class dest(models.Model):
    OWNER_NAME=models.CharField(max_length=100)
    COST=models.IntegerField(default=15)
    UPLOAD_HOUSE_IMAGE=models.ImageField(upload_to='new pics',default="NULL")
    UPLOAD_HOUSE_IMAGE2=models.ImageField(upload_to='new pics',default="NULL")
    UPLOAD_HOUSE_IMAGE3=models.ImageField(upload_to='new pics',default="NULL")
    ADDRESS=models.TextField(default="vignan")
    ADDRESS_URL=models.URLField(default="NULL")
    ENTER_LOCATION=models.URLField(max_length=2000,default='NULL')
    AREA=models.CharField(max_length=50,default="urban")
    
    STATE=models.CharField(max_length=50,default="krishna", choices= [             
            ('vizag', 'vizag'), 
            ('krishna', 'krishna'), 
            ('nellore', 'nellore'),  
            ('east godavari','east godavari'),
            ('chittor','chittor'),
            ('guntur','guntur'),  
            ('srikakulam','srikakulam'),
            ('kakinada','kakinada'),    
        ]       )

    def __str__(self):
        return self.OWNER_NAME

  

# admin created houses

class adminhouses(models.Model):
    IMAGE=models.ImageField(upload_to="pics",default="NULL")
    PRICE=models.IntegerField(default=250)
    PLACE=models.TextField(default="VIZAG")
class adminhouses2(models.Model):
    IMAGE=models.ImageField(upload_to="pics",default="NULL")
    PRICE=models.IntegerField(default=250)
    PLACE=models.TextField(default="VIZAG")

class adminhouses3(models.Model):
    IMAGE=models.ImageField(upload_to="pics",default="NULL")
    PRICE=models.IntegerField(default=250)
    PLACE=models.TextField(default="VIZAG")






class house(models.Model):
    type=models.CharField(max_length=200)
    cost=models.IntegerField(default=15)
    img=models.ImageField(upload_to='pics quaality')
    facility=models.TextField(default="3BHK") 
    phone=models.IntegerField(default=15,max_length=12)   


