from django.conf.urls import url, include
from maps.views import index

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import MushroomSpot, WorldBorder
from .views import MapLayer

app_name = 'maps'

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot, properties=('title', 'description', 'picture_url')), name='data')
    # url(r'^data.geojson$', GeoJSONLayerView.as_view(model=WorldBorder, properties=('name' )), name='data'),
    url(r'^data.geojson$', \
    	MapLayer.as_view(model=WorldBorder, properties=('name', 'pop2005' )), name='data'\
    	)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


