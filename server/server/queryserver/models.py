from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

# Create your models here.

class Session(models.Model):
    socid = models.IntegerField()

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
    boxinfo = JSONField()
