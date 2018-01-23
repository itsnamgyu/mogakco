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
    print("NEW CAFE MAN!!!!!!")
    print(request.POST['name'])
    return HttpResponseRedirect(reverse('cafe:index'))
