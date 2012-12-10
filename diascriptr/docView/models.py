from django.db import models
from datetime import datetime

# Create your models here.
"""
class User(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    pw = models.CharField(max_length = 128)
    date_created = models.DateTimeField()
    ip_adress = models.IPAddressField()


class Project(models.Model):
    user = models.ForeignKey('User')
    project_description = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    visibility = models.NullBooleanField()

    def __unicode__(self):
        return self.project_description


class Page(models.Model):
    date_created = models.DateTimeField()
    project = models.ForeignKey('Project')
    

    def __unicode__(self):
        return self.date_created
"""

class Transcriptions(models.Model):
       # page = models.ForeignKey('Page')
	content = models.CharField(max_length=1000)
	date_created = models.DateTimeField()

	def save(self):
		super(Transcriptions, self).save()

	def __unicode__(self):
		return self.content
