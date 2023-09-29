from django.contrib.auth.models import AbstractUser
from django.db import models 

class CustomUser(AbstractUser):
    username=models.CharField(max_length=50,blank=True,null=True,unique=True)
    email=models.EmailField(max_length=50,blank=True,null=True)
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    dob=models.DateField()
    password=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.username
    



