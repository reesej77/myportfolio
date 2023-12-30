from django.shortcuts import render
from .models import Project, Skill

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'main/skill_list.html', {'skills': skills})
# Create your views here.
