from django.db import models
from countries.models import Country


class Team(models.Model):
    name=models.CharField(max_length=255,null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    logo=models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.name