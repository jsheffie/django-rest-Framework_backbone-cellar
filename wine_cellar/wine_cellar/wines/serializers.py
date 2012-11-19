from django.forms import widgets
from rest_framework import serializers
from wine_cellar.wines import models

class WineSerializer( serializers.ModelSerializer ):
    """ Here we take advantage of the ModelSerializer ( analogous to ModelForm ) """
    class Meta:
        model = models.Wine
        fields = ( 'id', 'name', 'year', 'grapes', 'country', 'region', 'description', 'picture' )