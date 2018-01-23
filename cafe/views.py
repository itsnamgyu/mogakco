from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from cafe.models import Cafe


def list(request):
    cafes = Cafe.objects.all()
    return render(request, "cafe/list.html", {'cafes': cafes})


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
