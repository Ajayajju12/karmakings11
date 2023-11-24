from django.db import models

# Create your models here.
class Leaderboard(models.Model):
    score=models.IntegerField()
    username=models.CharField(max_length=255)
    rank=models.IntegerField()