from django.contrib import admin
from .models import Match,Matchresult

# Register your models here.
class MatchAdmin(admin.ModelAdmin):

    list_display=('country_one','country_two','datetime','venue')

admin.site.register(Match,MatchAdmin)

class matchResultAdmin(admin.ModelAdmin):

    list_display=('match','winner','runner')

admin.site.register(Matchresult,matchResultAdmin)

