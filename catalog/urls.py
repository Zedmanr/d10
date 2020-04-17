from django.urls import path

from catalog.views import car_view

urlpatterns = [
    path('', car_view, name='main'),
]