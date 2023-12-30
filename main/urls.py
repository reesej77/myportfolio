# main/urls.py

from django.urls import path
from .views import project_list, skill_list

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('skills/', skill_list, name='skill_list'),
]