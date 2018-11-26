from __future__ import unicode_literals
from __future__ import absolute_import
from django.shortcuts import render

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context_object_name = 'periods'
    return render(request, 'maps/index.html', {})