from django.shortcuts import render
from cafe.models import Cafe

def cafe_list(request):
    cafes = Cafe.objects.all()
    return render(request, "cafe/list.html", { 'cafes': cafes })
