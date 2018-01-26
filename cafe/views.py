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
            name_query = reduce(lambda q, f: q | Q(name__icontains=f), 
                                search_strings, Q())
            address_query = reduce(lambda q, f: q | Q(address__icontains=f),
                                   search_strings, Q())
            cafes = Cafe.objects.filter(name_query | address_query)

    else:
        search_string = ""
        cafes = Cafe.objects.all()

    return render(request, "cafe/list.html", {'cafes': cafes, 'search_string': search_string})



def create(request):
    return render(request, "cafe/create.html")


def add_review(request, cafe_pk):
    cafe = Cafe.objects.get(pk=cafe_pk)
    return render(request, "cafe/add_review.html", {'cafe': cafe})


def add_prices(request, cafe_pk):
    cafe = Cafe.objects.get(pk=cafe_pk)
    return render(request, "cafe/add_prices.html", {'cafe': cafe})


def submit_cafe(request):
    cafe = Cafe()
    try:
        cafe.name = request.POST['name']
        cafe.address = request.POST['address']
    except KeyError:
        print("Received an invalid cafe create form")
    else:
        cafe.save()

    return HttpResponseRedirect(reverse('cafe:index'))


def submit_review(request, cafe_pk):
    try:
        comment_string = request.POST['comment']
        comment = comment_string if comment_string else None

        cafe = Cafe.objects.get(pk=cafe_pk)
        cafe.review_set.create(
                plug=request.POST['plug'], wifi=request.POST['wifi'],
                comment=None)
    except (Cafe.DoesNotExist, KeyError):
        print("Received an invalid cafe create form")
    else:
        cafe.save()

    return HttpResponseRedirect(reverse('cafe:index'))


def submit_prices(request, cafe_pk):
    try:
        cafe = Cafe.objects.get(pk=cafe_pk)
        cafe.prices_set.create(americano=request.POST['americano'])
    except (Cafe.DoesNotExist, KeyError):
        print("Received an invalid cafe create form")
    else:
        cafe.save()

    return HttpResponseRedirect(reverse('cafe:index'))
