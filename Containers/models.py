from distutils.cmd import Command
from django.db import models

class dockerfile(models.Model):
    image = models.CharField(max_length=100)
    command = models.CharField(max_length=1000)

class dockerCompose(models.Model):
    version = models.FloatField()
    container_name = models.CharField(max_length=50)
    command = models.CharField(max_length=200)
    restart = models.CharField(max_length=20)
    env = models.CharField(max_length=200)
    volumes = models.CharField(max_length=200)
    ports = models.IntegerField()
    depends_on = models.CharField(max_length=200)