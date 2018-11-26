from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from . import models  as mushrooms_models 



class MapsAdmin(admin.ModelAdmin):
	list_display = ('name', 'location')

admin.site.register(mushrooms_models.MushroomSpot, LeafletGeoAdmin)
admin.site.register(mushrooms_models.mapas, LeafletGeoAdmin)
