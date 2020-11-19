from django import forms
from django.forms import ModelForm

from .models import Equipment, EquipmentCategory


class AddTools(forms.Form):
    machine = forms.CharField(label="Machine", max_length=100)
    tool_type = forms.CharField(label="tool type:", max_length=20)


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["category", "name", "quantity", "condition"]


class EquipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = ["name"]
