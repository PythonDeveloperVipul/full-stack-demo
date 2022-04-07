
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from . import forms
from .models import BuyCar, Car


class Home(ListView):
    model = Car
    template_name = 'car/home.html'
    paginate_by = 10
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['search_txt'] = self.request.GET.get("txtsearch", '')
        return context

    def get_queryset(self):
        query = self.request.GET.get("txtsearch", '')
        queryset = Car.objects.filter(
            Q(make__icontains=query) | Q(year__icontains=query)).order_by('-id')
        return queryset


class CarCreateView(View):
    def get(self, request):
        form = forms.CarForm()
        return render(request, 'car/car_data_insert.html', {'form': form})

    def post(self, request):
        form = forms.CarForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Thank You for Registration Our Car Buy Website.'
            return render(request, 'car/thanks_page.html', {'msg': msg})
        else:
            return render(request, 'car/car_data_insert.html', {'form': form})


class BuyCarView(View):
    def get(self, request, **kwrgs):
        cardata = Car.objects.get(id=kwrgs['pk'])
        form = forms.BuyCarForm()
        return render(request, 'car/buy_car.html', {'form': form, 'cardata': cardata})

    def post(self, request, **kwrgs):
        form = forms.BuyCarForm(request.POST)
        carobj = Car.objects.get(id=kwrgs['pk'])
        if form.is_valid():
            buy_name = form.cleaned_data['buy_name']
            buy_mobile = form.cleaned_data['buy_mobile']
            BuyCarobj = BuyCar(car=carobj, buy_name=buy_name,
                               buy_mobile=buy_mobile)
            BuyCarobj.save()

            carobj.car_status = 'Sold'
            carobj.save()
            msg = 'Thank You for Purchase Car. Dodgy Brothers Sortly Time to Communicated You.'
            return render(request, 'car/thanks_page.html', {'msg': msg})
        else:
            return render(request, 'car/buy_car.html', {'form': form, 'cardata': carobj})


class ThanksPage(TemplateView):
    template_name = 'car/thanks_page.html'


class CarStatusChange(View):
    def get(self, request, **kwrgs):
        carobj = Car.objects.get(id=kwrgs['pk'])
        carobj.car_status = 'Available'
        carobj.save()
        return redirect('/')



