import os

from django.urls import reverse
from django.conf import settings
# from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.gdal import DataSource
# from osgeo import osr
# import mapscript

# import validators

from djgeojson.fields import PolygonField
from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models

# STATUS_CHOICES = (
#     (mapscript.MS_OFF, "off"),
#     (mapscript.MS_ON, "on"),
#     (mapscript.MS_DEFAULT, "default")
# )

SHAPEFILE_EXTENSION = 'shp'

class MushroomSpot(models.Model):

	title = models.CharField(max_length=256)
	description = models.TextField()
	picture = models.ImageField()
	geom = PolygonField()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return str(self.title) 

	@property
	def picture_url(self):
		return self.picture.url

class mapas(models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	objects = GeoManager()
	def __unicode__(self):
		return self.name

	def __str__(self):
		return str(self.name) 

	class Meta:
		verbose_name_plural = 'Maps'
		verbose_name = 'Map'

	# title = models.CharField(max_length=256)
	# description = models.TextField()
# ---------------

