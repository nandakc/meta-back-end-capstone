from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.booking
        fields = '__all__'
