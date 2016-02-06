from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

# Create your models here.

class Soc(models.Model):
    url = models.CharField(max_length=256, default="")

class Session(models.Model):
    socid = models.ForeignKey(Soc)

class Video(models.Model):
    socid = models.ForeignKey(Soc)
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)

class Query(models.Model):
    answer = models.BooleanField(default=False)
    comment = models.TextField()
    sessionid = models.ForeignKey(Session)
    predicates = JSONField()

class Object(models.Model):
    label = models.CharField(max_length=256)
    sessionid = models.ForeignKey(Session)

class Box(models.Model):
    objectid = models.ForeignKey(Object)
    videoid = models.ForeignKey(Video)
    time = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    xlen = models.IntegerField(default=0)
    ylen = models.IntegerField(default=0)
