from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
"""
class User(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    pw = models.CharField(max_length = 128)
    date_created = models.DateTimeField()
    ip_adress = models.IPAddressField()

"""
class Project(models.Model):
    user = models.ForeignKey(User)
    project_name = models.CharField(max_length=40)
    project_description = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    visibility = models.NullBooleanField()

    def __unicode__(self):
        return self.project_name
#Have to fix it here somehow, there is a problem with MEDIA_ROOT and page_docs
def page_file_name(instance, filename):
    file_n = '/'.join(['page_docs', str(instance.project.id), filename])
    #file_n = '/'.join([str(instance.project.id), filename])
    print 'THE FILE UPLOAD PATH', file_n
    return file_n

class Page(models.Model):
    date_created = models.DateTimeField()
    project = models.ForeignKey('Project')
    page = models.FileField(upload_to=page_file_name)
    ##page_file_name)#'#page_docs/%Y/%m/%d')

    def __unicode__(self):
        return str(self.page)


class Transcriptions(models.Model):
       # page = models.ForeignKey('Page')
	content = models.CharField(max_length=1000)
	date_created = models.DateTimeField()

	def save(self):
		super(Transcriptions, self).save()

	def __unicode__(self):
		return self.content
