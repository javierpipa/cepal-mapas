from __future__ import unicode_literals
from __future__ import absolute_import
from django.shortcuts import render, redirect
from djgeojson.views import GeoJSONLayerView

# Create your views here.
def index(request):
    context_object_name = 'periods'
    return render(request, 'maps/index.html', {})


class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization