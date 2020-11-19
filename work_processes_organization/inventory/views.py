from django.shortcuts import render
from .forms import EquipmentForm, EquipmentCategoryForm
from .models import Equipment, EquipmentCategory

# Create your views here.
from django.http import Http404, HttpResponseRedirect, HttpResponse, FileResponse
from django.contrib.auth import *
from .models import *


def inventory(request):
    return render(request, 'inventory-menu.html')


def material(request):
    po = PurchaseOrder.objects.get_queryset()
    return render(request, 'material.html', {"pur_order": po})


def equipment(request):
    eq_add_form = EquipmentForm()
    eq_cat_form = EquipmentCategoryForm()
    equip = Equipment.objects.all()

    if request.method == 'POST':
        # create
        eq_cat_form = EquipmentCategoryForm(request.POST)
        if eq_cat_form.is_valid():
            eq_category = EquipmentCategory()
            eq_category.name = eq_cat_form.cleaned_data['name']
            eq_category.save()
            return HttpResponseRedirect('/inventory/equipment')

    return render(request, 'equipment.html',
                  {"list": None, "add_equipment": eq_add_form, "equip": equip, "eq_cat_form": eq_cat_form})


def table(request):
    po = PurchaseOrder.objects.get_queryset()
    return render(request, "table.html", {"po": po})
