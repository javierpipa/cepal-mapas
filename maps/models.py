import os

from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.gdal import DataSource


from djgeojson.fields import PolygonField
from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models
from django.core.validators import validate_comma_separated_integer_list
from maps import validators

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


class WorldBorder(models.Model):
	# Regular Django fields corresponding to the attributes in the
	# world borders shapefile.
	name = models.CharField(max_length=50)
	area = models.IntegerField()
	pop2005 = models.IntegerField('Population 2005')
	fips = models.CharField('FIPS Code', max_length=2)
	iso2 = models.CharField('2 Digit ISO', max_length=2)
	iso3 = models.CharField('3 Digit ISO', max_length=3)
	un = models.IntegerField('United Nations Code')
	region = models.IntegerField('Region Code')
	subregion = models.IntegerField('Sub-Region Code')
	lon = models.FloatField()
	lat = models.FloatField()

	mapobjs = models.ManyToManyField("MapObj", blank=True)

	# GeoDjango-specific: a geometry field (MultiPolygonField)
	geom = models.MultiPolygonField()

	# Returns the string representation of the model.
	def __str__(self):
		return self.name

class MapServerColor(models.Model):
	red = models.IntegerField(blank=True, null=True, validators=[validators.validate_integer_color])
	green = models.IntegerField(blank=True, null=True, validators=[validators.validate_integer_color])
	blue = models.IntegerField(blank=True, null=True, validators=[validators.validate_integer_color])
	hex_string = models.CharField(max_length=9, blank=True, validators=[validators.validate_hex_color])
	attribute = models.CharField(max_length=255, blank=True)

	def build(self):
		return mapscript.colorObj(self.red, self.green, self.blue)

	def __unicode__(self):
		result = u"RGB({}, {}, {})".format(self.red, self.green,
											self.blue)
		return result

class MapObj(models.Model):
	MAP_SIZE = (800, 600)
	IMAGE_TYPE_CHOICES = (
		("png", "png"),
	)
	# UNITS_CHOICES = (
	#     (mapscript.MS_DD, "Decimal degrees"),
	# )
	name = models.CharField(max_length=255, help_text="Unique identifier.")
	status = models.SmallIntegerField()
	# choices=STATUS_CHOICES
	projection = models.PositiveSmallIntegerField(
	    default= 4326, help_text="EPSG code of the map projection"
	)
	# units = models.SmallIntegerField(choices=UNITS_CHOICES)
	# size = models.CommaSeparatedIntegerField(help_text="Map size in pixel units",
	# 										max_length=10)
	size = models.CharField(help_text="Map size in pixel units", max_length=10,validators=[validate_comma_separated_integer_list])
    # cell_size = models.FloatField(help_text="Pixel size in map units.",
    #                               blank=True, null=True)
    # extent = models.ForeignKey("RectObj", help_text="Map's spatial extent.")
    # # font_set
	image_type = models.CharField(max_length=10, choices=IMAGE_TYPE_CHOICES)
	image_color = models.ForeignKey("MapServerColor",
									help_text="Initial map background color.",
									null=True, blank=True, on_delete=models.CASCADE)
	# countries = models.ForeignKey("WorldBorder", blank=True, null=True, on_delete=models.CASCADE) 
    # layers = models.ManyToManyField("LayerObj", null=True, blank=True,
    #                                 through="MapLayer")
    # # legend
    # # metadata (see what parameters refer to each service)
    # # ows_title is the same as the map's name
    # ows_sld_enabled = models.BooleanField(default=True)
    # ows_abstract = models.TextField(blank=True)
    # ows_enable_request = models.CharField(max_length=255, default="*")
    # ows_encoding = models.CharField(max_length=20, default="utf-8")
    # ows_onlineresource does not need to be editable
    # ows_srs uses the same projection as the map and does not need to be editable

  #   def build(self):
  #       """
  #       Build a mapObj
  #       """

  #       uri = reverse("wms_endpoint")
  #       m = mapscript.mapObj()
  #       m.name = self.name
  #       m.setProjection("init=epsg:{}".format(self.projection))
  #       m.shapepath = ""
  #       m.units = self.units
  #       m.setMetaData("ows_title", self.name)
  #       m.setMetaData("ows_onlineresource",
  #                     "http://{}{}".format(settings.HOST_NAME, uri))
  #       m.setMetaData("wms_srs", "EPSG:{}".format(self.projection))
  #       m.setMetaData("wms_enable_request", self.ows_enable_request)
  #       m.setMetaData("wms_encoding", "utf-8")
  #       m.imagetype = "png"
  #       m.extent = self.extent.build()
  #       m.setSize(*self.MAP_SIZE)
  #       if self.image_color is not None:
  #           m.imageColor = self.image_color.build()
  #       else:
  #           m.imageColor = mapscript.colorObj(255, 255, 255)
  #       for layer in self.layers.all():
  #           m.insertLayer(layer.build())
  #       return m

  #   def _available_layers(self):
  #       return ', '.join((la.name for la in self.layers.all()))
  #   available_layers = property(_available_layers)

  #   def __unicode__(self):
		# return self.name