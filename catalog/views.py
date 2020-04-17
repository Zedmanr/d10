from django.db.models import Q
from django.shortcuts import render

from catalog.models import Car
from catalog.forms import CarForm


def car_view(request):
    form = CarForm()
    if not list(request.GET.items()):
        cars = Car.objects.all()
        return render(request, 'catalog/index.html', {'form': form, 'cars': cars})
    else:
        cars = Car.objects.filter(
            Q(manufacturer__icontains=request.GET.get('manufacturer')) &
            Q(model_of_auto__icontains=request.GET.get('model_of_auto')) &
            Q(year_of_issue__gte=request.GET.get('year_of_issue')) &
            Q(transmission__icontains=request.GET.get('transmission')) &
            Q(colour__icontains=request.GET.get('colour'))
        )
        return render(request, 'catalog/index.html', {'form': form, 'cars': cars})