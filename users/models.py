from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
   email=models.EmailField(max_length=255,unique=True,null=True)
   dob=models.DateField(null=True)
   bio=models.TextField(null=True)



   def  __str_(self):
      return self.username