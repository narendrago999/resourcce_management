from django.urls import path
from .views import *
urlpatterns = [
    path('', availableResource, name="availableResource"),
    path('resources', Resource, name="Resource"),
]
