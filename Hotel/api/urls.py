from django.urls import path
from .views import *
urlpatterns = [
    path('service/', ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/', ServiceUpdateView.as_view(), name='service_detail'),

    path('excursions/',ExcursionsCreateView.as_view(), name='excursions_create'),
    path('excursions/<int:pk>/', ExcursionsUpdateView.as_view(), name='excursions_detail'),

    path('tours/<int:pk>/', TourUpdateView.as_view()),
    path('tours/', TourCreateView.as_view()),


    path('cart/',MyOfficeCreateView.as_view(), name='cart_create'),
    path('cart/<int:pk>/', MyOfficeDetailView.as_view()),

    path('countries/',CountryCreateView.as_view(), name='country_create'),
    path('countries/<int:pk>/', CountryUpdateView.as_view(), name='country_update')

]
