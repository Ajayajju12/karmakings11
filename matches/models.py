from django.db import models
from countries.models import Country
from players.models import player

# Create your models here.
class Match(models.Model):
    country_one=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    country_two=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    datetime=models.DateTimeField(null=True,blank=True)
    venue=models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.country_one
    
class Matchresult(models.Model):
    match=models.ForeignKey(Match,on_delete=models.SET_NULL,blank=True)
    winner=models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True)
    runner=models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True)