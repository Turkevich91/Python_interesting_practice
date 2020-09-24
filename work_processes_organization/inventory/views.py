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


def m_equipment(request):
    # TODO create DB
    return HttpResponse('HttpResponse: m_equipment view, no data yet')


def p_equipment(request):
    # TODO create DB
    return HttpResponse('HttpResponse: p_equipment view, no data yet')


def table(request):
    po = PurchaseOrder.objects.get_queryset()
    return render(request, "table.html", {"po": po})
