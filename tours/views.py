from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from tours.data import tours, departures
import random


class MovieView(View):
    def get(self, request, *args, **kwargs):
        random_tours = dict()

        while True:
            el = random.choice(list(tours.keys()))
            if el not in random_tours:
                random_tours[el] = tours[el]
                if len(random_tours) == 6:
                    break

        return render(request, 'index.html', {'departures': departures, 'random_tours': random_tours})


class DepartureView(View):
    def get(self, request, departure):
        tours_depart = dict()
        price_list = list()
        night_list = list()

        for key in tours:
            if tours[key]['departure'] == departure:
                tours_depart[key] = tours[key]

        for key in tours_depart:
            price_list.append(int(tours_depart[key]['price']))
            night_list.append(int(tours_depart[key]['nights']))

        context = {
            'departures': departures,
            'tours_depart': tours_depart,
            'tour_qt': len(tours_depart),
            'price_min': min(price_list),
            'price_max': max(price_list),
            'nights_min': min(night_list),
            'nights_max': max(night_list),
            'depart': departures[departure]
        }

        return render(request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            raise Http404
        depart = departures[tours[id]['departure']]
        return render(request, 'tours/tour.html', {'departures': departures, 'tours': tours[id], 'depart': depart})


def custom_handler404(request, exception):
    return HttpResponseNotFound("""<h1>Ошибки – это наука, помогающая нам двигаться вперед. У. Ченнинг </h1>
    <h2> 404 Not Found</h2> """)


def custom_handler500(request):
    return HttpResponseServerError("""<h1>Мечта моя разбилась на сотню маленьких мечтаний! Г. Симпсон </h1>
    <h2> 500 Server Error</h2> """)
