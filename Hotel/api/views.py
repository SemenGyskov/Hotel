from django.shortcuts import render
from django.views.generic import *
from rest_framework import generics
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import *
from .models import *


class ServiceCreateView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

class ServiceUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]




class ExcursionsCreateView(CreateAPIView):
    queryset = Excursions.objects.all()
    serializer_class = ExcursionsSerializer
    permission_classes = [IsAdminUser]

class ExcursionsUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Excursions.objects.all()
    serializer_class = ExcursionsSerializer
    permission_classes = [IsAdminUser]




class TourCreateView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticated]

class TourUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticated]


class MyOfficeCreateView(CreateAPIView):
    queryset = MyOffice.objects.all()
    serializer_class = MyOfficeSerializer
    permission_classes = [IsAdminUser]

class MyOfficeDetailView(RetrieveAPIView):
    queryset = MyOffice.objects.all()
    serializer_class = MyOfficeSerializer

class MyOfficeUpdateView(RetrieveUpdateAPIView):
    queryset = MyOffice.objects.all()
    serializer_class = MyOfficeSerializer
    permission_classes = [IsAdminUser]


class CountryCreateView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class CountryUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]
