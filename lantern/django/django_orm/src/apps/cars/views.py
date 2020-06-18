from django.shortcuts import render
from django.views import View

from apps.cars.models import Car


# Create your views here.
class CarList(View):
    def get(self, request):
        cars = Car.objects.order_by('-model')
        return render(request, 'car_list.html', {'cars': cars})
