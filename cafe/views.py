from django.shortcuts import render
from cafe.models import Cafe

def list(request):
    cafes = Cafe.objects.all()
    return render(request, "cafe/list.html", { 'cafes': cafes })

def create(request):
    return render(request, "cafe/create.html")
