from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
import os
from .models import Project



class StoreProjectsView(View):
    def get(self, request):
        # busco el archivo json
        if os.path.isfile('projects.json'):
            with open('projects.json', 'r') as f:
                projects = json.load(f)
        else:
            return HttpResponse('No projects found', status=404)

        # guardo los proyectos en la base de datos
        
        for project in projects:
            # guardo el proyecto
            project_obj = Project.objects.create(
                number=project['number'],
                name=project['name'],
                type=project['type'],
                region=project['region'],
                typology=project['typology'],
                owner=project['owner'],
                investment=project['investment'],
                date=project['date'],
                status=project['status'],
                map=project['map'],
            )

        return HttpResponse('Projects saved', status=200)

class ProjectsView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'projects_info.html', {'projects': projects})
                    