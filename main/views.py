from django.shortcuts import render
from cafe.models import *

# Create your views here.
def displayMainPage(request):
    return render(request, 'main/main.html', {})


def displaySearchPage(request):
    return render(request, 'main/search.html', {})


def displayResultPage(request, keyword):
    cafes = CafeInfo.objects.get(name__contains=keyword)
    return render(request, 'main/result.html', {'cafes': cafes})
