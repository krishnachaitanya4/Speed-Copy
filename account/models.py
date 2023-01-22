from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length = 12)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    pin = models.CharField(max_length=7,null=True,blank=True)
    district = models.CharField(max_length=15,null=True,blank=True)
    area = models.CharField(max_length=50,null=True,blank=True)
    street = models.CharField( max_length=50,null=True,blank=True)
    door_no = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.user_id)
    
    