from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=21)
    Age=models.IntegerField()
    Place=models.CharField(max_length=24)
    Email=models.EmailField()
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Password=models.CharField(max_length=8)
    
class Image(models.Model):
    Name=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Age=models.IntegerField()
