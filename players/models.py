from django.db import models
from countries.models import Country
#from players.models import player
from matches.models import Match


# Create your models here.
class player(models.model):
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    matches=models.IntegerField(null=True,blank=True)
    runs=models.IntegerField(null=True,blank=True)
    batting_style=models.CharField(max_length=255,null=True,blank=True,choices=[
        ('left-hand bat','left-hand bat'),
        ('right-hand bat','right-hand bat'),
 ])
    bowling_style=models.CharField(max_length=255,null=True,blank=True,choices=[
        ('right-arm fast','right-arm fast'),
        ('left-arm fast','left-arm fast'),
        ('right-arm offbreak','right-arm offbreak'),
        ('left-arm offbreak','left-arm offbreak'),
    ])
    player_type=models.CharField(max_length=255,null=True,blank=True,choices=[
        ('batsman','batsmen'),
        ('bowler','bowler'),
        ('allrounder','allrounder'),
        ('wicketkeeper','wicketkeeper')
    ])
    is_captain=models.BooleanField(null=True,blank=True)
    def str(self):
        return self.name
    
    class playermatchpoints(models.model):
        player=models.ForeignKey(Player,on_delete=models.SET_NULL)
        match=models.ForeignKey(Match,on_delete=models.SET_NULL)
        points=models.IntegerField(null=True,blank=True)