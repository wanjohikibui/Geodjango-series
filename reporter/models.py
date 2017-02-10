from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Incidences(models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	objects = models.GeoManager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural =" Incidences"

class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.counties

    class Meta:
        verbose_name_plural = 'Counties'
    	

