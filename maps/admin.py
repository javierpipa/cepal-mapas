from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from . import models  as models 

class Vars_WorldBorder(admin.TabularInline):
    model = models.WorldBorder
    extra = 1


class MapObjAdmin(admin.ModelAdmin):
	model = models.MapObj
	# fieldsets = [
 #        (None, {'fields': (('name', 'status', 'projection' ),)}),
        
 #    ]
	# inlines = [Vars_WorldBorder,]
class MapsAdmin(admin.ModelAdmin):
	list_display = ('name', 'location')

admin.site.register(models.MushroomSpot, LeafletGeoAdmin)
admin.site.register(models.mapas, LeafletGeoAdmin)
admin.site.register(models.WorldBorder, LeafletGeoAdmin)
admin.site.register(models.MapServerColor)
admin.site.register(models.MapObj, MapObjAdmin )


