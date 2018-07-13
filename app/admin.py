from django.contrib import admin

from . import models

admin.site.register(models.Address)
admin.site.register(models.Team)
admin.site.register(models.FieldLocation)
admin.site.register(models.TeamPlayer)
admin.site.register(models.TeamAddress)
admin.site.register(models.Player)
admin.site.register(models.Field)