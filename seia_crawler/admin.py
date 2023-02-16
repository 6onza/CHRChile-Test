from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'type', 'region', 'typology', 'owner', 'investment', 'date', 'status', 'map')

admin.site.register(Project, ProjectAdmin)