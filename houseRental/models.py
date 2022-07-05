from email.policy import default
from django.db import models

# Create your models here.
class dest(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=15)
    img=models.ImageField(upload_to='pics',default="NULL")
    collegeinfo=models.TextField(default="vignan")


class house(models.Model):
    type=models.CharField(max_length=200)
    cost=models.IntegerField(default=15)
    facility=models.TextField(default="3BHK") 
    phone=models.IntegerField(default=15)   

class user_record(models.Model):
    name = models.TextField(max_length=20,null=False)
    location = models.TextField(null=False)
    user_dp = models.ImageField(default="")


