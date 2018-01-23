from functools import reduce

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from cafe.models import Cafe


def list(request):
    if 'search_string' in request.GET:
        search_string = request.GET['search_string']
        if search_string == "":
            cafes = Cafe.objects.all()
        else:
            search_strings = search_string.replace("역", " ").split()
            name_query = reduce(lambda q, f: q | Q(name__icontains=f), search_strings, Q())
            address_query = reduce(lambda q, f: q | Q(address__icontains=f), search_strings, Q())
            cafes = Cafe.objects.filter(name_query | address_query)

    else:
        search_string = ""
        cafes = Cafe.objects.all()

    return render(request, "cafe/list.html", {'cafes': cafes, 'search_string': search_string})


def create(request):
    return render(request, "cafe/create.html")


def submit(request):
    cafe = Cafe()
    try:
        cafe.name = request.POST['name']
        cafe.address = request.POST['address']
        cafe.americano = request.POST['americano']
        cafe.plug = request.POST['plug']
        cafe.wifi = request.POST['wifi']
    except KeyError:
        print("Received an invalid cafe create form")
    else:
        cafe.open_sat = 0
        cafe.open_sun = 0
        cafe.open_weekday = 0
        cafe.close_sat = 0
        cafe.close_sun = 0
        cafe.close_weekday = 0
        cafe.save()

    return HttpResponseRedirect(reverse('cafe:index'))
