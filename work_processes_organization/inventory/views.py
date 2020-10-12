from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponseRedirect, HttpResponse, FileResponse
from django.contrib.auth import *
from .models import *


def inventory(request):
    return render(request, 'inventory-menu.html')


def material(request):
    po = PurchaseOrder.objects.get_queryset()
    return render(request, 'material.html', {"pur_order": po})


def machine_equipment(request):
    # TODO create DB
    return HttpResponse('HttpResponse: machine_equipment view, no data yet')


def personal_equipment(request):
    # TODO create DB
    return HttpResponse('HttpResponse: personal_equipment view, no data yet')


def table(request):
    po = PurchaseOrder.objects.get_queryset()
    return render(request, "table.html", {"po": po})
