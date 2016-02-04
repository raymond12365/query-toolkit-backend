from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

# Create your models here.

class Session(models.Model):
    socid = models.IntegerField()

class Soc(models.Model):
    url = models.CharField(max_length=256)

class Video(models.Model):
    socid = models.IntegerField()
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)

class Query(models.Model):
    answer = models.BooleanField(default=False)
    comment = models.TextField()
    sessionid = models.IntegerField()
    predicates = JSONField()

class Object(models.Model):
    label = models.CharField(max_length=256)
    sessionid = models.IntegerField()

class Box(models.Model):
    objectid = models.IntegerField()
    videoid = models.IntegerField()
    time = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    xlen = models.IntegerField()
    ylen = models.IntegerField()
