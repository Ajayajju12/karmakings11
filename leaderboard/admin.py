from django.contrib import admin
from.models import Leaderboard

# Register your models here.
class leaderboardAdmin(admin.ModelAdmin):
    list_display=('score','rank','username')

admin.site.register(Leaderboard,leaderboardAdmin)
