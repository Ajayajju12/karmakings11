from django.contrib import admin
from .models import player

# Register your models here.
class playerAdmin(admin.ModelAdmin):
    list_display=('name','number','matches','runs','batting_style','bowling_style','player_type')

admin.site.register(player,playerAdmin)