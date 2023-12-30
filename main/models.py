from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as needed

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # Add more fields as needed
# Create your models here.
