from django.db import models

class Country(models.Model):
    name=models.CharField(max_length=255,null=True)
    code=models.IntegerField(unique=True,null=True)


    def __str__(self):
        return self.name
