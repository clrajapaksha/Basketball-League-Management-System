from django.contrib import admin
from teams.models import Player, Team
from users.models import User

admin.site.register(User)
admin.site.register(Player)
admin.site.register(Team)
