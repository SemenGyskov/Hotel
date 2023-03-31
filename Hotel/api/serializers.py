from rest_framework import serializers
from .models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ExcursionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursions
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class MyOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyOffice
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'