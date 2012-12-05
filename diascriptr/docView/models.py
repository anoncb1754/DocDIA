from django.db import models
from datetime import datetime

# Create your models here.
class Transcriptions(models.Model):
	content = models.CharField(max_length=1000)
	date_created = models.DateTimeField()

	def save(self):
		super(Transcriptions, self).save()

	def __unicode__(self):
		return self.content